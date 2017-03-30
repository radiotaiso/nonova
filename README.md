[![Build Status](https://travis-ci.org/ucoria-itexico/nonova.svg?branch=master)](https://travis-ci.org/ucoria-itexico/nonova) <- I still have no idea how travis works, working on implementing that
# nonova
Sick of nova? this is your tool.

## Getting started
Nonova uses nova-cli to input items in Nova easy, quick and painless from your favorite terminal.

#### Changelog 03/16/2017

We're happy to anounce version 1.0. Save and read activities from file implemented.

### Prerequisites

You can install the packages either global or in an virtualenv. It's up to you.

In any case there's requirements.txt with covers it.

### Installation

1. Clone the project to your desired location
2. Install prerequiste packages

### Usage

After cloning and installing go to the project's folder and run:
```python
python nonova.py --help
```

The purpose of the tool is to easily fill "ini" files that contain your activities

You can generate different ini files for different days of the week and thus retrieve and upload those activities in another time.

*REMEMBER* You can only upload activites for _the same day_

Follow the steps to provide your credentials (which will be stored locally on the same folder)
this will also get your OS in order to use the right compliled nova-cli.

You can query your assigned projects using:
```python
python nonova.py -p
```

To get the list of categories for the task run:
```
python nonova.py -C
```

To add a new item to your nova you just need to run:
```
python nonova.py -a
```
And provide the information requested, after the first item entered previous options given will be set as default
so if you just press `enter` it will use the bracketed information.

## Everything else

General extra information for reference or whatever you want it to be.

### Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

### Authors

[Uriel Coria](# "lol you're already here")

[Toño "Evidentemente" Herran](https://github.com/antonioherran "his github")

[Karly Garcia](https://github.com/KarlyGrCm "Karly's stuff")


### License

This project is licensed under the GPL-3.0 - see the [LICENSE.md](LICENSE.md) file for details

#### Such wow
Did you really read everything? that's pretty cool! 

KTHXBAI
