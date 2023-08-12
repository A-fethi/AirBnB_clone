<h1> 0x00. AirBnB clone - The console </h1>

<h2> Synopsis </h2>

The Airbnb clone project for which we are creating a copy of the [Airbnb](https://www.airbnb.com/).
Only some features will be implemented and will be listed below once completed.

<h2> Features </h2>

<h3> Command Interpreter </h3>

<h4> Description </h4>

The Command Interpreter is used to manage the whole application's functionality from the command line, such as:
+ Crete a new object.
+ Retrieve an object from a file, database, etc.
+ Execute operation on objects. e.g. Count, compute statistics, etc.
+ Update object's attributes.
+ Destroy an object

<h4> Usage </h4>

To launch the console application in interactive mode simply run:

`console.py `

or to use the non-interactive mode run:

`echo "your-command-goes-here" | ./console.py`

<h4> Commands </h4>

Commands | Description | Usage
-------- | ----------- |-------- |
**help** or **?**| Displays the documented commands. | **help**
**quit**     | Exits the program. | **quit**
**EOF**      | Ends the program. Used when files are passed into the program. | N/A
**create**  | Creates a new instance of the \<class_name\>. Creates a Json file with the object representation. and prints the id of created object. | **create** \<class_name\>
**show**    | Prints the string representation of an instance based on the class name and id. | **show** \<class_name class_id\>
**destroy** | Deletes and instance base on the class name and id. | **destroy** \<class_name class_id\>
**all** | Prints all string representation of all instances based or not on the class name | **all** or **all** \<class_name class_id\>
**update** | Updates an instance based on the class name and id by adding or updating attribute | **update** \<class_name class_id key value\>

<h2> Tests </h2>

If you wish to run at the test for this application all of the test are located
under the **test/** folder and can execute all of them by simply running:

`python3 -m unittest discover tests`

from the root directory.
