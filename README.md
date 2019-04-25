# Control Pane for CarControl


## Usage
This Web-Application is based on Python Django and provides an Form for the 2 necessary Values to control the EV3-Car
- **Speed:** Value in % ranging from -100 to 100.
This Value does represent the amount of Power sent to the Motor of the car. Positive values represent a forward motion, negative values a backward motion.

- **Steering:** Value in % ranging from -100 to 100.
This Value will move the Steerin motor to it's percentage amount of the maximum angle to the left (negative values) and the right (positive values)

With **"Send It!"** a mqtt message is created from the posted formdata and sent to the message broker.

## Installation

Links:
- [Sourcecode Repository an GitHub](https://www.github.com/ev3-showcase/webapp_carcontrol)
- [MCS PaaS Demo Platform](https://master-aotp012.mcs-paas.io:8443/console/)

To get this Application running within OpenShift following steps are necessary:

1. Login into web Console using the provided Link
2. Create a new project or select an existing one
3. go to the catalog. Select the tab Languages > Python > Select the "Python" without any additions.
4. Within the now opened information box click "Next" to go to Configuration
5. Enter following Information: 
- Select you Project from dropdown, 
- Enter an Application name (do only use numbers, lowercase characters and the - symbol, this name is lateron used for url-resolution and therefor needs to fit the criteria)
- For git-repository enter the link's url for the sourcecode repository from above
- click the link to go to advanced options
- Search for the "Deployment config" part.
Enter following information:

Name | Value
------------ | -------------
DISABLE_MIGRATE|True

Click "Create" on the bottom.

6. Now you can click "Overview" on the Left and follow the Buildprocess if you expand the newly created application tile in the main window. After the build has finished the image will be deployed. If the Container Circle does show a blue ring, the app is ready. Now you can click the route shown at the top of the tile to open the app within a new tab.