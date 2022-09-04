
## Welcome to the Bolts Control App.

This app will calculate the quantities of six different metric-sized bolts left in the **inventory** by the end of the day.

This will take into consideration two inputs from the user:

    1o. The quantities of bolts that are being used in the manufacturing (work-in-progress), also known as **WIP**
    2o. The Quantities of bolts that have been damaged or are in bad conditions (**scrapped**)

In the scrapped condition, the bolts are taken out of manufacturing to be repaired (in case of corrosion) or recovered (in case of pitting rust). Normally, bolts that have been subject to humidity environment could have pitting of rusts on their surfaces and in the worst case scenario, the corrosion itself, meaning that some small parts of the bolts might present lack of material. In both cases, they must be repaired. The process of application of some coating can provide a layer of protection against rusts and corrosion by acting as a physical barrier between the metal parts and oxidizing elements in the environment. One common method is galvanization.

![Responsive Mockup](/images/am_i_responsive.png)

[Live website here](https://bolt-control.herokuapp.com/)

## How the app works

Firstly, let's introduce the metric-size bolt system applied in this app.




By the end of the day of a manufacturing company, the bolts that have been used to manufacture any type of equipment, for instance, are designated in the **WIP** (work-in-progress) and are inputed firstly in the app.

Then, a second input of quantities of bolts in bad condition are **scrapped** and removed from the manufacturing.
The user may have also input the bolts that have been recovered already, so in terms of notation:

* bolts been removed as scrapped: **positve** notation
* bolts been recovered from scrappage: **negative** notation





This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!