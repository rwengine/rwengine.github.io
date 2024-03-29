## What is OpenRW
OpenRW is an open-source game engine that attempts to re-implement the engine used in the classic video game Grand Theft Auto III (GTA III), first released in 2001. With the purpose of enabling better compatibility with modern systems and ensuring that it remains possible to play the game in the future.

The primary goal of the project is to reach “Version 1.0”, this would mean:
* Fully implementing the original gameplay
* Compatible with all data formats used in the game
* Compatible with modern gamepads where possible
* Able to load save game files from the game
* Run with community made mods that only change game data
* Run natively on Windows, Linux and macOS

OpenRW would not aim for Version 1.0 to re-create any obvious bugs such as crashes or situations where the game becomes impossible to progress.

Other features, which would not be needed for Version 1.0 include:
* Enhanced support for user modification
* Changes to the gameplay
* Multiplayer

Features like these will not be accepted into OpenRW at present, as these don’t contribute to the primary goal. Once Version 1.0 has been reached a “new” version of OpenRW may be forked that contains these kinds of features.

## Do I need GTA III to play OpenRW?
In short: Yes.

OpenRW is simply a game engine that is compatible with the original game, it has no assets of its own. In order to play GTA III using  OpenRW you must own the game and have the data installed on your system. If you need a copy of the game it’s available on [Steam](http://store.steampowered.com/app/12100/).

It is theoretically possible to develop a completely new game, without any of the assets or content from GTA III, however no such project is currently under way.

## Can I play OpenRW now?
In its current state it is not possible to complete the game using OpenRW, or make any significant progress through the game. There are many bugs that need to be fixed and features that need to be developed before it becomes possible to play anything with OpenRW. The latest version of OpenRW will always be available from the source code [repository](https://github.com/rwengine/openrw).

## Can I play OpenRW on my macOS / Linux computer?
Yes. OpenRW runs on macOS and Linux, as well as some BSDs.

## Why make OpenRW?
Beyond technical curiosity, OpenRW exists to conserve the game and ensure it is playable into the future by improving compatibility with modern systems and allowing future developers to make the engine compatible with whatever systems may exist in the future.

In addition to conservation it may also offer a platform for others to build 3D action games in the future.

## Can I contribute to OpenRW?
Yes, development of OpenRW is open, you can follow along and contribute via the GitHub [project page](https://github.com/rwengine/openrw). Also drop into the IRC channel, `#openrw` @ [irc.libera.chat](https://web.libera.chat/#openrw).

## What licence is OpenRW released under
The OpenRW engine is released under the GNU General Public License Version 3.

## Who is working on OpenRW?
The project is developed in an open and collaborative manner, anyone who wishes to contribute code or documentation is able to send changes via a pull request to the github [repository](https://github.com/rwengine/openrw).

## Will it be possible to play Vice City with OpenRW?
The current priority of the project is to implement support for playing GTA III. Once this is completed it will be clear how much extra work will be required to fully support Vice City in addition to III. The work may need to be done in a fork of OpenRW dedicated to Vice CIty, or it may be unfeasible for one reason or another.

## What is the story?
Development on OpenRW was started by tsjost and danhedron in 2013,  where it began as a simple model viewer that became a map viewer. Over time OpenRW has gained new features such as physics, vehicles and pedestrians, and a script machine that make more of the game accessible via the OpenRW engine. Now it is possible to start a new game or load a save game within OpenRW and interact with the world.
At present, development is performed in the open where anyone is free to contribute to the project via the github repository.

