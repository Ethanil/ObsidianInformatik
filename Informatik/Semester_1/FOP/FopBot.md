[[FOP]]Bot ist ein Git-Repository welches das Lernen von [[Java]] erleichtern soll

# Robot-Befehle
```java
- turnLeft()
	- Turns the robots body to the left
- move()
	- Move the robot one step forward in the current direction
- putCoin()
	- Puts down one coin at the current position
- pickCoin()
	- Picks up one coin at the current position
- printTrace()
	- Prints the robot trace
		- "Robot(Name) is at (X,Y) facing Richtung with Z coins (Turned On/Off)."
- getDirection()
	- @return the current direction of the robot
- getNumverOfCoins()
	- @return the number of coins the robot possesses
- hasAnyCoins()
	- @return true if the robot has any coins
- isFacingUp() / isFacingDown() / isFacingRight() / isFacingLeft()
	- @return true if the robot is facing up/down/right/left
- setPrintTrace(bool)
	- enables/disables printing a trace to System.out after each action of the 	
	robot
- isPrintTraceEnabled()
	- @return true if print tracing is enabled
- turnOff()
	- Turn off the robot
- isTurnedOff()/isTurnedOn()
	- @return true if the robot is turned off/on
- isNextToACoin()
	- @return true if the robot is standing on a coin/if at least one coin is at 
	the same position as the robot's position
- isNextToARobot()
	- @return true if at least another robot is at the same position as the 
	robot's position
- setId(String)/getId()
	- Sets/@return the id of the robot
- setImageId(String)/getImageId()
	- Sets/@return the image id of the robot
- setX(int)/getX() & setY(int)/getY()
	- Sets@return the robot's x-coordinate/y-coordinate
- setField(int,int)
	- Sets the robot's field (x,y)
- isFrontClear()
	- @return true if the robot is not facing an object that is standing in the 
	way eg. wall)
```