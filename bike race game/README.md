# 🚴 Bike Race Game with Streamlit

An exciting bike racing game built with Python and Streamlit featuring obstacles, power-ups, multiple difficulty levels, and a beautiful web interface.

## Features

- 🚴 **Dynamic Gameplay**: Control a bike and avoid obstacles
- 🎯 **Multiple Difficulty Levels**: Easy, Medium, Hard, and Expert modes
- ⚡ **Power-ups**: Speed boost, invincibility, and bonus points
- 📊 **Score Tracking**: Real-time score and high score tracking
- 🎨 **Modern UI**: Beautiful gradient design with responsive layout
- 📱 **Responsive Design**: Works on desktop and mobile devices
- 🎮 **Game Controls**: Pause/resume, new game, and difficulty selection

## Game Elements

- 🚴 **Bike**: Your character (red, turns yellow when invincible)
- 🚗 **Cars**: Obstacles to avoid
- 🚙 **SUVs**: Obstacles to avoid
- 🚌 **Buses**: Obstacles to avoid
- 🚛 **Trucks**: Obstacles to avoid
- 🏍️ **Motorcycles**: Obstacles to avoid
- ⚡ **Speed Boost**: Temporary speed increase
- 🛡️ **Shield**: Temporary invincibility
- 💎 **Diamond**: Extra points

## Installation

1. **Clone or download the files** to your local machine

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game**:
   ```bash
   streamlit run bike_race_game.py
   ```

4. **Open your browser** and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

## How to Play

1. **Start the Game**: Click "New Game" to begin
2. **Control the Bike**: Use the Left/Right buttons to move
3. **Avoid Obstacles**: Dodge cars, trucks, and other vehicles
4. **Collect Power-ups**: Grab power-ups for bonuses:
   - ⚡ Speed boost: Move faster temporarily
   - 🛡️ Shield: Become invincible temporarily
   - 💎 Diamond: Get extra points
5. **Survive**: Try to survive as long as possible and achieve high scores

## Game Controls

### Main Controls
- **⬅️ Left**: Move bike to the left
- **➡️ Right**: Move bike to the right
- **New Game**: Start a fresh game
- **Pause/Resume**: Pause or resume the current game
- **Reset High Score**: Clear the saved high score

### Difficulty Levels
- **Easy**: Slow speed, good for beginners
- **Medium**: Moderate speed, balanced gameplay
- **Hard**: Fast speed, challenging gameplay
- **Expert**: Very fast speed, for experienced players

## Game Features

### Power-ups
- **⚡ Speed Boost**: Increases bike speed for a limited time
- **🛡️ Invincibility**: Makes you immune to obstacles temporarily
- **💎 Diamond**: Gives bonus points immediately

### Progressive Difficulty
- **Level System**: Game gets harder as you progress
- **Increasing Speed**: Obstacles move faster at higher levels
- **More Obstacles**: Spawn rate increases with level
- **Score Multiplier**: Higher levels give more points

### Visual Indicators
- 🚴 **Red Bike**: Normal state
- 🚴 **Yellow Bike**: Invincible state
- ⚡ **Speed Boost**: Active speed boost indicator
- 🛡️ **Shield**: Active invincibility indicator

## Technical Details

- **Framework**: Streamlit for web interface
- **Game Logic**: Pure Python with collision detection
- **State Management**: Streamlit session state for persistent data
- **Styling**: Custom CSS for modern appearance
- **Responsive Design**: Works on various screen sizes

## File Structure

```
bike_race_game/
├── bike_race_game.py   # Main game file
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Customization

You can easily customize the game by modifying the following parameters in `bike_race_game.py`:

- **Game Speed**: Adjust the `speed_map` dictionary
- **Obstacle Types**: Modify the `obstacle_types` list
- **Power-up Types**: Change the `powerup_types` list
- **Visual Elements**: Update the emoji characters
- **Difficulty Scaling**: Adjust level progression parameters

## Game Mechanics

### Collision Detection
- Rectangle-based collision detection
- Precise hitbox calculations
- Invincibility bypasses collisions

### Scoring System
- **Base Score**: 10 points per obstacle avoided
- **Power-up Bonus**: 100 points for diamond collection
- **Level Bonus**: Higher levels give more points

### Level Progression
- **Level 1**: Basic difficulty
- **Level 2+**: Increased speed and spawn rates
- **Progressive Scaling**: Continuous difficulty increase

## Future Enhancements

- **Sound Effects**: Audio feedback for actions
- **Multiple Bikes**: Different bike characters
- **Track Variations**: Different road environments
- **Multiplayer**: Competitive racing mode
- **Achievements**: Unlockable achievements
- **Leaderboard**: Global score tracking
- **Custom Skins**: Different bike appearances
- **Special Events**: Limited-time challenges

## Troubleshooting

- **Game not starting**: Make sure all dependencies are installed
- **Slow performance**: Try reducing the game speed or difficulty
- **Display issues**: Check your browser compatibility
- **Controls not responding**: Refresh the page and try again

## Browser Compatibility

- **Chrome**: Full support
- **Firefox**: Full support
- **Safari**: Full support
- **Edge**: Full support
- **Mobile browsers**: Responsive design works on mobile

## Performance Tips

- **Close other tabs**: Free up browser resources
- **Lower difficulty**: Start with Easy mode for better performance
- **Refresh page**: If game becomes unresponsive
- **Check internet**: Ensure stable connection for Streamlit

## License

This project is open source and available under the MIT License.

---

Enjoy racing your bike! 🚴💨 