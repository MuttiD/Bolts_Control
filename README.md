
## Welcome to the Bolts Control App.

This app will calculate the quantities of six different metric-sized bolts left in the **inventory** by the end of the day.

This will take into consideration two inputs from the user:

1. The quantities of bolts that are being used in the manufacturing (work-in-progress), also known as **WIP**
2. The Quantities of bolts that have been damaged or are in bad conditions (**scrapped**)

In the scrapped condition, the bolts are taken out of manufacturing to be repaired (in case of corrosion) or recovered (in case of pitting rust). Normally, bolts that have been subject to humidity environment could have pitting of rusts on their surfaces and in the worst case scenario, the corrosion itself, meaning that some small parts of the bolts might have lack of material. In both cases, they must be repaired. The process of application of some coating can provide a layer of protection against rusts and corrosion by acting as a physical barrier between the metal parts and oxidizing elements in the environment. One common method is galvanization.

![Responsive Mockup](/images/am_i_responsive.png)

[Live website here](https://bolt-control.herokuapp.com/)

## How the app works

__The metric-size standard for bolts__

Firstly, let's introduce the metric-size bolt system applied in this app.

Please see below a chart showing a sample of metric-size (MXX M for metric and XX for nominal size) bolts and their specifications. The highlited ones are those we used for our app.

![metric_size_bolts](/images/metric_size_bolts.png)

__Features of the App__

Now that we have introduced the metric system of bolts, let's jump into the working functions of the app.

By the end of the day of a manufacturing company, the bolts that have been used to assemble an equipment, for instance, are designated in the **WIP** (work-in-progress) area and are inputed firstly in the app.

Then, a second input of quantities of bolts, the ones in bad condition are **scrapped** and removed from the manufacturing.
The user may have also input the bolts that have been recovered already, so in terms of notation:

* bolts been removed as scrapped: **positve** notation
* bolts been recovered from scrappage: **negative** notation

Once the program has received both inputs (WIP and SCRAP) the program will calculate the final inventory figures, following the formula:

**Inventory = WIP - scrap**

The values inputed by the user as well as the result of the inventory are stored in a Google Drive Account under The Google Sheets Program, on a daily basis.

__The Terminal__

In the terminal, the user will input six values of WIP and scrap in the format of numbers, separated by comma: 

For example: **12,23,19,21,29,18**

If the user mistakenly added a letter or insuficiently numbers, the program will return a message with the error listed and will keep running until the user input the correct numbers, which it will be validated.

![data_validated](/images/data_validated.png)

Once the data are valid, the program then runs the inventory function, which will calculate and store the data in a Google Sheets File.

__The Results__

Let's suppose the user input a WIP of 12,25,14,18,21,23 and scrap of -5,3,4,-2,0,5.

Then the app will do the following steps, in that order:

1. Validate the data provided
2. Update WIP worksheet
3. Update scrap worksheet
4. calculate inventory
5. Update inventory worksheet

![WIP_results](/images/WIP_results.png)
![scrap_results](/images/scrap_results.png)
![inventory_results](/images/inventory_result.png)


## Testing

I have manually tested this project several times by doing the following:

* Passed the code through PEP8 checker and confirmed there are no problems
* Given invalid inputs such as: letters, insufficient numbers, etc
* I tested it in my local terminal and the Code Institute Heroku Terminal


## Validator Testing

* The PEP8 checker [PEP8](http://pep8online.com/about) was used to check for errors.
    * No errors were returned.

![PEP8_passed](/images/PEP8_passed.png)

## Bugs
No bugs left behind


## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

* Steps for deployment:
    * Create a new Heroku app
    * Set the builbacks in this order
        1. `heroku/python`
        2. `heroku/nodejs`
    * Create the following *Config Var*:
        * `PORT`.Set this to `8000`
        * copy `CREDS` and then paste the JSON into the value field.
    * Link the Heroku app to the repository
    * Click Connect
    * Click on **Deploy**


## Credits 

I would like to thank [CodeInstitute](https://codeinstitute.net/ie/) for the valuable help throughout all the channels of help (Slack, Mentorship, Tutoring).

I also took some hours going through the contents of [Python](https://docs.python.org/3.10/contents.html).