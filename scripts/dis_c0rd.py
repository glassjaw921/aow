import discord
from discord.ext.commands import Bot
from discord.ext import commands
import pymysql

#client = discord.Client()
bot_prefix = "!"
client = commands.Bot(command_prefix=bot_prefix)
token = ''
HOST = ''
USER = ''
PASSWORD = ''
DB = ''
PORT = 3306
#connection = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB, port=PORT)
Bot.remove_command(client, "help")
def connect():
    try:
        connection = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB, port=PORT)
        return connection
    except Exception as e:
        print(e)


@client.event
async def on_ready():
    print("Bot online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))



@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")


@client.command(pass_context=True)
async def hug(ctx, message=None):
    if message == None:
        await client.say("hugs @{0}".format(ctx.message.author))
    else:
        await client.say("hugs {0}".format(message))


@client.command(pass_context=True)
async def help(ctx):
    await client.say(""
    "!help   \tFor HELP because you obviously need it"
    "\n!profile  Checks your profile or do !profile @username"
    "\n!set  \t  To set your POSQ address. EXAMPLE : !set POSQ_ADDRESS_HERE "
    #"\n!new  \tTo update your current Poseidon address. EXAMPLE : !new POSQ_ADDRESS_HERE"
    "\n!ping \t Ping the bot"
    "\n!hug  \t Hug's @userName")


@client.command(pass_context=True)
async def set(ctx, message):
    

    # verify address length
    if (len(message) != 34):
        # address is invalid
        msg = 'Invalid address. Address is not the correct length, must be 34 characters'
        await client.say(msg)

    elif (len(message) == 34):  # address is correct
        # set users discord id number, posq address and message author name
        sql_id_number = ctx.message.author.id
        posqAddress = message
        author = ctx.message.author

        # check to see if user already has a database entry
        
        try:
            #connect
            dbhandler = connect().cursor()
            checkDB = dbhandler.execute("SELECT address from test WHERE user_id = '{}'".format(author))
            currentPOSQAddress = dbhandler.fetchone()

            if (checkDB):

                msg = 'Your current POSQ address is  :  {} ' \
                      '\nwould you like to set a new one? !new NEW_ADDRESS_HERE '.format(currentPOSQAddress[0])
                await client.say(msg)

            else:
                try:  # insert author, posqAddress, and sql_id_number into db


                    dbhandler.execute("INSERT INTO test (`user_id`, `address`, `id_number`, `total`) "
                                      "VALUES ('{0}', '{1}', '<@{2}>', '1000');".format(author, posqAddress, sql_id_number))
                    connect().commit()
                    msg = '{0} has been set as your posq address'.format(posqAddress)
                    await client.say(msg)
                    print(author, "DB user created")
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

    else:
        msg = 'Invalid address. Please enter a Poseidon address beginning with Q'
        await client.say(msg)


@client.command(pass_context=True)
async def new(ctx, message):
    # verify address length
    if (len(message) != 34):
        # address is invalid
        msg = 'Invalid address. Address is not the correct length, must be 42 characters'
        await client.say(msg)

    elif (len(message) == 34):  # address is correct
        # set users discord id number, posq address and message author name
        posqAddress = message
        author = ctx.message.author
        sql_id_number = ctx.message.author.id


        try:  # insert posq address into db

            dbhandler = connect().cursor()
            dbhandler.execute("UPDATE test SET address = '{0}' WHERE id_number = '<@{1}>'".format(posqAddress, sql_id_number))
            connect().commit()
            #update db
            print(author, "posq address updated")
            
        except Exception as e:
            print(e)
        
        msg = '{0} has been set as your posq address'.format(posqAddress)
        await client.say(msg)

    else:
        msg = 'Invalid address. Please enter a Poseidon address beginning with Q'
        await client.say(msg)

@client.command(pass_context=True)
async def profile(ctx, message=None):
    author = ctx.message.author
    print(author)
    try:
        #connect to db
        dbhandler = connect().cursor()
        checkdb = dbhandler.execute("SELECT address from test WHERE user_id = '{0}'".format(author))
        posqAddress = dbhandler.fetchone()
        # verify there is an entry    
        if (checkdb):
            
            dbhandler.execute("SELECT total from test WHERE user_id = '{0}'".format(author))
            posq = dbhandler.fetchone()
            
            print(author, "checked profile")
            msg = 'User = @{0} \nPOSQ address = {1} \nPOSQ CREDIT = {2}'.format(author, posqAddress[0], posq[0])
            await client.say(msg)
            
        else:
            msg = 'User {0} has not created a profile yet. use !help or !set'.format(author)
            await client.say(msg)

    except Exception as e:
        print(e)
        msg = 'User {0} does not have a profile'.format(author)
        await client.say(msg)


client.run(token)
