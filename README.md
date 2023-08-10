# **Friday - Music Bot for Discord**

### Video Demo : https://youtu.be/tbH5oVkNC0Y



# **Description** :

Friday is a entertainment purpose discord bot focusing mainly on Music. Adding Friday to your server simply makes it easy for you to listen to any track you wish without having to choose through _different options_ before you can start listening.

# **Table Of Contents :**

1. Dependencies
2. Files
3. Working
4. Commands
5. Example of Execution

# **Dependencies :**

- [discord.py](https://discordpy.readthedocs.io/en/stable/index.html)
- [youtube_dl](https://github.com/ytdl-org)

# **Files :**

- bot.py
- README.md

# **Working :**

Below mentioned are some commands and how you can use them after connecting Friday to your Server.
Some examples are given as to how you can execute each command. The sentence following '>>' is the reply you should be expecting after running that command.

### **Commands :**

All of Friday's commands are prefixed with 'a$'. Simply add 'a$' followed by a command specified below.

1. Friday
2. Join
3. Play
4. Pause
5. Resume
6. Queue
7. Display
8. Stop
9. Disconnect

### **Example of Execution :**

#### Friday :

A simple boot up command that you can execute to check if the bot is ready for execution. If this command works, then the others should too!

    EXECUTION:
        a$Friday
        >> Friday, at your Service!

#### Join :

Use this to get Friday to join a voice channel. [NOTE: You should be in a voice channel before using this command]

    EXECUTION:
        a$join
        >> Voice Chat activated!

> The following commands can be executed only after using 'Join'

#### Play :

Use this to get Friday to play a song. _[Note: You cannot use Song Names]_

    EXECUTION:
      a$play <url of the song>
      >> Now Playing <name of the song>

#### Pause :

Pauses a song or soundtrack.

    EXECUTION:
      a$pause
      >> Queue Paused.

#### Resume :

Resumes a song or soundtrack.

    EXECUTION:
      a$resume
      >> Resuming Queue..

#### Queue :

Use this to get Friday to add a song to queue. _[Note: You cannot use Song Names]_

    EXECUTION:
      a$queue <url of the song>
      >> Song added to Queue..

#### Display:

Displays the current music queue.

    EXECUTION:
      a$display
      >> <song 1>
      >> <song 2>

#### Stop :

Stops a song or soundtrack.

    EXECUTION:
      a$stop
      >> Music Stopped.

#### Disconnect :

Disconnects Friday from Voice channel.

    EXECUTION:
      a$disconnect
      >> Voice chat Deactivated!
