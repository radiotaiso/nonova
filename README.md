# nonova
Sick of nova? this is your tool.

## Getting started
Nonova uses nova-cli to input items in Nova easy, quick and painless from your favorite terminal.

Version 1 is almost ready and in continious development (not as quick as we'd like but hey we have work to do besides this `¯\_(ツ)_/¯`)

### Prerequisites

+ Python 2.x
+ ArgParse

### Installation

1. Clone the project to your desired location
2. Install ArgParse and ConfigParser
    ```
    pip install argparse
    ```
### Usage

After cloning and installing go to the project's folder and run:
```python
python nonova.py -c config.ini
```
Follow the steps to provide your credentials (which will be stored locally on the same folder)
this will also get your OS in order to use the right compliled nova-cli.

You can query your assigned projects using:
```python
python nonova.py -p
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

[Uriel Coria](https://github.com/ucoria-itexico/ "lol you're already here")
[Toño "Evidentemente" Herran](https://github.com/antonioherran "his github")

### License

This project is licensed under the GPL-3.0 - see the [LICENSE.md](LICENSE.md) file for details

#### Wow
Did you really read everything? that's pretty cool! 
