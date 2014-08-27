# Alfred Input Method Editor

A Input method program based on Alfred workflow and Google Input Tools

* What it _can_ do?
	1. Can be used as input method to type characters other than English.
    2. Save time from switching between input methods if only want to write a few characters.
    3. Support multiple languages' input methods.
* What it _can't_ do?
    1. For massive input, please consider using input method software.
	2. Work offline.
* How to _install_ it?
	1. Have access to the Internet.
    2. Download and install Alfred [Powerpack](http://www.alfredapp.com/powerpack/).
    3. Download and open the workflow.

###Screenshots


###Usage:
* `ime [input] [number of alternatives]`
	* `↕` Choose an option.
    * `tab ↹` Update the input with partial result for furthur input recognition.
    * `enter ↵` Select the final result, paste it to the input field of the front application.
    * `[number of alternatives]` Number of possible alternatives provided. Enter a large number, like 30, if a word cannot be found in current list. The default number is 10, which can be modified with command `imeconfig num` (see below). 
* `imeconfig [option]`
	* `imeconfig lang` Choose language.
    * `imeconfig num [integer]` Set default number of possible alternatives.
    
    
    
###Supported Language:
* Chinese(simplified)
* Japanese 
	
    For inquiries of new language support, please open an issue.

###Copyright, Licensing and Thanks

* Alfred-workflow([Git Repo](https://github.com/deanishe/alfred-workflow)) are licensed under the [MIT](http://opensource.org/licenses/MIT) and [Creative Commons Attribution-NonCommercial licences](https://creativecommons.org/licenses/by-nc/4.0/legalcode) respectively.
* Workflow Icon([Source](http://commons.wikimedia.org/wiki/File:GoogleIMENewLogo.png)) comes from Google Pinyin 
* [Goolge Input method](http://www.google.com/inputtools/)
* All other code and documents are licensed under [MIT]{http://opensource.org/licenses/MIT}
