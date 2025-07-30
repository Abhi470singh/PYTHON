import streamlit as st
import numpy as np
import random
import time
from typing import List, Tuple, Optional
import json

# Page configuration
st.set_page_config(
    page_title="Bike Race Game",
    page_icon="🚴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #e74c3c;
        margin-bottom: 2rem;
    }
    .game-stats {
        display: flex;
        justify-content: space-around;
        margin: 1rem 0;
        padding: 1rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        color: white;
    }
    .stat-box {
        text-align: center;
        padding: 0.5rem;
    }
    .stat-value {
        font-size: 1.5rem;
        font-weight: bold;
    }
    .game-area {
        background: linear-gradient(180deg, #87CEEB 0%, #98FB98 100%);
        padding: 20px;
        border-radius: 15px;
        margin: 1rem 0;
        border: 3px solid #2c3e50;
    }
    .road {
        background: #696969;
        height: 400px;
        position: relative;
        border-radius: 10px;
        overflow: hidden;
        margin: 1rem 0;
    }
    .lane-divider {
        position: absolute;
        width: 100%;
        height: 2px;
        background: white;
        animation: moveRoad 0.5s linear infinite;
    }
    .bike {
        position: absolute;
        font-size: 2rem;
        z-index: 10;
    }
    .obstacle {
        position: absolute;
        font-size: 1.5rem;
        z-index: 5;
    }
    .powerup {
        position: absolute;
        font-size: 1.5rem;
        z-index: 5;
        animation: pulse 1s infinite;
    }
    @keyframes moveRoad {
        0% { transform: translateY(-100%); }
        100% { transform: translateY(100%); }
    }
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.2); }
    }
    .controls-info {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .game-over {
        text-align: center;
        font-size: 2rem;
        color: #e74c3c;
        font-weight: bold;
        margin: 1rem 0;
    }
    .success-message {
        text-align: center;
        font-size: 1.5rem;
        color: #27ae60;
        font-weight: bold;
        margin: 1rem 0;
    }
    .difficulty-btn {
        margin: 0.2rem;
        padding: 0.5rem 1rem;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-weight: bold;
    }
    .difficulty-btn.active {
        background: #3498db;
        color: white;
    }
    .difficulty-btn:not(.active) {
        background: #ecf0f1;
        color: #2c3e50;
    }
</style>
""", unsafe_allow_html=True)

class BikeRaceGame:
    def __init__(self):
        self.road_width = 600
        self.road_height = 400
        self.bike_width = 40
        self.bike_height = 60
        self.reset_game()
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.bike_x = self.road_width // 2
        self.bike_y = self.road_height - 80
        self.bike_speed = 5
        self.obstacles = []
        self.powerups = []
        self.score = 0
        self.level = 1
        self.game_over = False
        self.paused = False
        self.invincible = False
        self.invincible_timer = 0
        self.speed_boost = False
        self.speed_boost_timer = 0
        self.obstacle_speed = 3
        self.obstacle_spawn_rate = 0.02
        self.powerup_spawn_rate = 0.005
        self.lane_divider_y = 0
    
    def update_bike_position(self, direction: str):
        """Update bike position based on input"""
        if self.game_over or self.paused:
            return
        
        if direction == "left" and self.bike_x > 50:
            self.bike_x -= self.bike_speed
        elif direction == "right" and self.bike_x < self.road_width - 90:
            self.bike_x += self.bike_speed
    
    def spawn_obstacle(self):
        """Spawn a new obstacle"""
        if random.random() < self.obstacle_spawn_rate:
            obstacle_types = ["🚗", "🚙", "🚌", "🚛", "🏍️"]
            obstacle_type = random.choice(obstacle_types)
            x = random.randint(50, self.road_width - 90)
            self.obstacles.append({
                'x': x,
                'y': -50,
                'type': obstacle_type,
                'width': 40,
                'height': 40
            })
    
    def spawn_powerup(self):
        """Spawn a powerup"""
        if random.random() < self.powerup_spawn_rate:
            powerup_types = ["⚡", "🛡️", "💎"]
            powerup_type = random.choice(powerup_types)
            x = random.randint(50, self.road_width - 90)
            self.powerups.append({
                'x': x,
                'y': -50,
                'type': powerup_type,
                'width': 30,
                'height': 30
            })
    
    def update_obstacles(self):
        """Update obstacle positions"""
        for obstacle in self.obstacles[:]:
            obstacle['y'] += self.obstacle_speed
            if obstacle['y'] > self.road_height:
                self.obstacles.remove(obstacle)
                self.score += 10
    
    def update_powerups(self):
        """Update powerup positions"""
        for powerup in self.powerups[:]:
            powerup['y'] += self.obstacle_speed
            if powerup['y'] > self.road_height:
                self.powerups.remove(powerup)
    
    def check_collisions(self):
        """Check for collisions between bike and obstacles"""
        if self.invincible:
            return
        
        bike_rect = {
            'x': self.bike_x,
            'y': self.bike_y,
            'width': self.bike_width,
            'height': self.bike_height
        }
        
        # Check obstacle collisions
        for obstacle in self.obstacles:
            if self.rect_collision(bike_rect, obstacle):
                self.game_over = True
                return
        
        # Check powerup collisions
        for powerup in self.powerups[:]:
            if self.rect_collision(bike_rect, powerup):
                self.apply_powerup(powerup['type'])
                self.powerups.remove(powerup)
    
    def rect_collision(self, rect1: dict, rect2: dict) -> bool:
        """Check collision between two rectangles"""
        return (rect1['x'] < rect2['x'] + rect2['width'] and
                rect1['x'] + rect1['width'] > rect2['x'] and
                rect1['y'] < rect2['y'] + rect2['height'] and
                rect1['y'] + rect1['height'] > rect2['y'])
    
    def apply_powerup(self, powerup_type: str):
        """Apply powerup effect"""
        if powerup_type == "⚡":
            self.speed_boost = True
            self.speed_boost_timer = 50
            self.bike_speed = 8
        elif powerup_type == "🛡️":
            self.invincible = True
            self.invincible_timer = 100
        elif powerup_type == "💎":
            self.score += 100
    
    def update_powerups_timers(self):
        """Update powerup timers"""
        if self.invincible_timer > 0:
            self.invincible_timer -= 1
            if self.invincible_timer == 0:
                self.invincible = False
        
        if self.speed_boost_timer > 0:
            self.speed_boost_timer -= 1
            if self.speed_boost_timer == 0:
                self.speed_boost = False
                self.bike_speed = 5
    
    def update_level(self):
        """Update game level based on score"""
        new_level = (self.score // 500) + 1
        if new_level > self.level:
            self.level = new_level
            self.obstacle_speed += 0.5
            self.obstacle_spawn_rate += 0.005
    
    def update_lane_divider(self):
        """Update lane divider animation"""
        self.lane_divider_y = (self.lane_divider_y + 20) % self.road_height
    
    def get_game_state(self) -> dict:
        """Get current game state for display"""
        return {
            'bike_x': self.bike_x,
            'bike_y': self.bike_y,
            'obstacles': self.obstacles,
            'powerups': self.powerups,
            'lane_divider_y': self.lane_divider_y,
            'score': self.score,
            'level': self.level,
            'game_over': self.game_over,
            'paused': self.paused,
            'invincible': self.invincible,
            'speed_boost': self.speed_boost
        }

def load_high_score():
    """Load high score from session state"""
    if 'high_score' not in st.session_state:
        st.session_state.high_score = 0
    return st.session_state.high_score

def save_high_score(score: int):
    """Save high score to session state"""
    if score > st.session_state.high_score:
        st.session_state.high_score = score

def main():
    st.markdown('<h1 class="main-header">🚴 Bike Race Game</h1>', unsafe_allow_html=True)
    
    # Initialize game
    if 'bike_game' not in st.session_state:
        st.session_state.bike_game = BikeRaceGame()
    
    game = st.session_state.bike_game
    
    # Sidebar controls
    with st.sidebar:
        st.header("Game Controls")
        
        # Difficulty selection
        st.subheader("Difficulty")
        difficulty = st.selectbox(
            "Select difficulty:",
            ["Easy", "Medium", "Hard", "Expert"],
            index=0
        )
        
        # Speed mapping
        speed_map = {"Easy": 0.1, "Medium": 0.05, "Hard": 0.03, "Expert": 0.02}
        game_speed = speed_map[difficulty]
        
        # Game controls
        st.subheader("Controls")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("New Game"):
                game.reset_game()
                st.rerun()
        
        with col2:
            if st.button("Pause/Resume"):
                game.paused = not game.paused
                st.rerun()
        
        # High score reset
        if st.button("Reset High Score"):
            st.session_state.high_score = 0
            st.rerun()
        
        # Instructions
        st.subheader("How to Play")
        st.markdown("""
        - Use A/D or Left/Right arrows to move
        - Avoid obstacles (cars, trucks, etc.)
        - Collect power-ups for bonuses:
          - ⚡ Speed boost
          - 🛡️ Invincibility
          - 💎 Extra points
        - Survive as long as possible!
        """)
    
    # Main game area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Game stats
        high_score = load_high_score()
        
        st.markdown(f"""
        <div class="game-stats">
            <div class="stat-box">
                <div>Score</div>
                <div class="stat-value">{game.score}</div>
            </div>
            <div class="stat-box">
                <div>High Score</div>
                <div class="stat-value">{high_score}</div>
            </div>
            <div class="stat-box">
                <div>Level</div>
                <div class="stat-value">{game.level}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Game area
        st.markdown('<div class="game-area">', unsafe_allow_html=True)
        
        # Display game over message
        if game.game_over:
            st.markdown('<div class="game-over">Game Over!</div>', unsafe_allow_html=True)
            save_high_score(game.score)
            
            if st.button("Play Again"):
                game.reset_game()
                st.rerun()
        
        # Display paused message
        elif game.paused:
            st.markdown('<div class="success-message">Game Paused</div>', unsafe_allow_html=True)
            if st.button("Resume"):
                game.paused = False
                st.rerun()
        
        # Display game
        else:
            # Road visualization
            st.markdown(f"""
            <div class="road" style="width: {game.road_width}px; height: {game.road_height}px;">
                <div class="bike" style="left: {game.bike_x}px; top: {game.bike_y}px; color: {'yellow' if game.invincible else 'red'};">
                    🚴
                </div>
            """, unsafe_allow_html=True)
            
            # Display obstacles
            for obstacle in game.obstacles:
                st.markdown(f"""
                <div class="obstacle" style="left: {obstacle['x']}px; top: {obstacle['y']}px;">
                    {obstacle['type']}
                </div>
                """, unsafe_allow_html=True)
            
            # Display powerups
            for powerup in game.powerups:
                st.markdown(f"""
                <div class="powerup" style="left: {powerup['x']}px; top: {powerup['y']}px;">
                    {powerup['type']}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Game controls
            st.markdown("### Controls")
            col_left, col_right = st.columns(2)
            
            with col_left:
                if st.button("⬅️ Left"):
                    game.update_bike_position("left")
                    st.rerun()
            
            with col_right:
                if st.button("➡️ Right"):
                    game.update_bike_position("right")
                    st.rerun()
            
            # Power-up status
            if game.invincible:
                st.info("🛡️ Invincible!")
            if game.speed_boost:
                st.info("⚡ Speed Boost!")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Game information
        st.markdown("""
        <div class="controls-info">
            <h4>Game Information:</h4>
            <ul>
                <li>🚴 Red bike: Your character</li>
                <li>🚗🚙🚌🚛🏍️: Obstacles to avoid</li>
                <li>⚡ Speed boost: Move faster temporarily</li>
                <li>🛡️ Invincibility: Cannot be hit temporarily</li>
                <li>💎 Diamond: Extra points</li>
                <li>Yellow bike: Invincible mode</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Game loop
    if not game.game_over and not game.paused:
        # Update game state
        game.spawn_obstacle()
        game.spawn_powerup()
        game.update_obstacles()
        game.update_powerups()
        game.check_collisions()
        game.update_powerups_timers()
        game.update_level()
        game.update_lane_divider()
        
        # Auto-rerun for continuous gameplay
        time.sleep(game_speed)
        st.rerun()

if __name__ == "__main__":
    main() 