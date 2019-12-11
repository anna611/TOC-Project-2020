# TOC Project 2020(流浪動物認養平台)
### 這次Project主要想法是為了提倡動物領養代替購買，結合全國動物收容管理系統，去找出等待領養的浪浪們。
## Setup

### Prerequisite
* Python 3.6
* Pipenv
* Facebook Page and App
* HTTPS Server

#### Install Dependency
```sh
pip3 install pipenv

pipenv --three

pipenv install

pipenv shell
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)
	* [Note: macOS Install error](https://github.com/pygraphviz/pygraphviz/issues/100)

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

#### a. Ngrok installation
* [ macOS, Windows, Linux](https://ngrok.com/download)

or you can use Homebrew (MAC)
```sh
brew cask install ngrok
```

**`ngrok` would be used in the following instruction**

```sh
ngrok http 8000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py
```

#### b. Servo

Or You can use [servo](http://serveo.net/) to expose local servers to the internet.
### Upload project to Heroku

1. Add local project to Heroku project

	heroku git:remote -a {HEROKU_APP_NAME}

2. Upload project

	```
	git add .
	git commit -m "Add code"
	git push -f heroku master
	```

3. Set Environment - Line Messaging API Secret Keys

	```
	heroku config:set LINE_CHANNEL_SECRET=your_line_channel_secret
	heroku config:set LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
	```

4. Your Project is now running on Heroku!

	url: `{HEROKU_APP_NAME}.herokuapp.com/callback`

	debug command: `heroku logs --tail --app {HEROKU_APP_NAME}`

5. If fail with `pygraphviz` install errors

	run commands below can solve the problems
	```
	heroku buildpacks:set heroku/python
	heroku buildpacks:add --index 1 heroku-community/apt
	```

## Finite State Machine
![](https://i.imgur.com/I7uDz4l.png)


## Usage
The initial state is set to `user`.
* user
	* Input: "start"
		![](https://i.imgur.com/vEByMmm.jpg)

* start
    * Input: "fsm"
		![](https://i.imgur.com/uu75IEo.jpg)
    
    
    * Input: "我要領養"
        ![](https://i.imgur.com/96v5l88.jpg)

* choose1
    * Input: "狗" (去爬蟲全國動物收容系統得到的資料，按更多資訊會前往網站)
    * ![](https://i.imgur.com/4BvUMCU.jpg)

    * Input: "貓"
    ![](https://i.imgur.com/ThB2RIi.jpg)

* dog
    * Input: "下載圖片"
     ![](https://i.imgur.com/A5OR3nt.jpg)


    * Input: "下一個"
     ![](https://i.imgur.com/EVxGcuY.jpg)


* cat
    * Input: "下載圖片"
     ![](https://i.imgur.com/NCTK5Qv.jpg)

    * Input: "下一個"
     ![](https://i.imgur.com/mSBuHVN.jpg)
* pic
    * Input: "下一個"
    ![](https://i.imgur.com/mSBuHVN.jpg)

