import discord
from discord.ext.commands import Bot
from discord.ext import commands
import pymysql

bot_prefix = "!"
client = commands.Bot(command_prefix=bot_prefix)
token = ""  # this is for testnet
HOST = '127.0.0.1'
USER = ''
PASSWORD = ''
DB = 'poseidon'
Bot.remove_command(client, "help")
def connect():
    try:
        connection = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB)
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
    print("PING/PONG")

@client.command(pass_context=True)
async def hug(ctx, message=None):
    if message == None:
        await client.say("hugs @{0}".format(ctx.message.author))
    else:
        await client.say("hugs {0}".format(message))
    print("HUG")

@client.command(pass_context=True)
async def help(ctx):
    await client.say("!help   \tFor HELP because you obviously need it"
    "\n!profile  Checks your profile or do !profile @username"
    "\n!set  \t  Register with Bot. EXAMPLE : !set POSQ_ADDRESS"
    "\n!new  \tTo update your current Poseidon address. EXAMPLE : !new POSQ_ADDRESS"
    "\n!ping \t Ping the bot"
    "\n!hug  \t Hug's @userName"
    "\n"
    "\nAll commands start with !"
    "\nYour POSQ address starts with a Q and is 34 characters long")
    print("HELP")




@client.command(pass_context=True)
async def set(ctx, message=None):
    posqAddress = message
    author = ctx.message.author
    sql_id_number = ctx.message.author.id
    if (message == None):
        msg = 'invalid command. try again - !set POSEIDON_ADDRESS'
        await client.say(msg)
        print(author, "SET BLANK")
    else:
        conn = connect()
        # verify address length
        if (len(message) != 34):
            # address is invalid
            msg = 'Invalid address. Address is not the correct length, must be 34 characters'
            await client.say(msg)
            print(ctx.message.author, " tried invalid address")

        elif (len(message) == 34):  # address is correct
            # set users discord id number, posq address and message author name

            if message[:1] == 'Q':
                # check to see if user already has a database entry
                dbhandler = conn.cursor()

                try:
                    checkDB = dbhandler.execute("SELECT address from poseidon WHERE user_id = '{}'".format(author))
                    currentPOSQAddress = dbhandler.fetchone()

                    if (checkDB): #USER ALREADY HAS A DATABASE ENTRY

                        msg = 'Your current POSQ address is  :  {} ' \
                              '\nwould you like to set a new one? !new NEW_ADDRESS_HERE '.format(currentPOSQAddress[0])
                        await client.say(msg)
                        print(ctx.message.author, " ALREADY HAS AN ADDRESS")


                    else:
                        try:  # insert posq address into db
                            dbhandler.execute("INSERT INTO poseidon (`user_id`, `address`, `id_number`, `total`) "
                                              "VALUES ('{0}', '{1}', '<@{2}>', '100');".format(author, posqAddress, sql_id_number).encode('utf-8'))
                            conn.commit()
                            msg = '{0} has been set as your posq address'.format(posqAddress)

                            await client.say(msg)
                            print(author, "---- NEW DB USER CREATED ----")

                        except Exception as e:
                            print(e)

                except Exception as e:
                    print(e)

            else:
                msg = 'Invalid address. Please enter a Poseidon address beginning with Q'
                await client.say(msg)
                print(author, " tried invalid NEW address")
        else:
            msg = 'Invalid address. Please enter a Poseidon address beginning with Q'
            await client.say(msg)
            print(ctx.message.author, " tried invalid address")


@client.command(pass_context=True)
async def new(ctx, message=None):

    author = ctx.message.author
    sql_id_number = ctx.message.author.id
    if (message == None):
        msg = 'invalid command. try again - !new POSEIDON_ADDRESS'
        await client.say(msg)
        print(author, "NEW BLANK")
    else:
        conn = connect()
        # verify address length
        if (len(message) != 34):

            # address is invalid
            msg = 'Invalid address. Address is not the correct length, must be 34 characters'
            await client.say(msg)
            print(author, " tried invalid NEW address")

        elif (len(message) == 34):  # address is correct
            # UPDATE user's discord
            if message[:1] == 'Q':

                dbhandler = conn.cursor()
                checkdb = dbhandler.execute("SELECT address from test WHERE user_id = '{0}'".format(author))
                posqAddress = message

                if (checkdb): # USER ALREADY HAS A DATABASE ENTRY


                    try:  # insert POSQ address into db
                        dbhandler = conn.cursor()
                        dbhandler.execute("UPDATE test SET address = '{0}' WHERE id_number='<@{1}>'".format(posqAddress, sql_id_number))
                        conn.commit()
                        msg = '{0} has been set as your new POSQ address'.format(posqAddress)
                        await client.say(msg)
                        print(author, "posq address updated")

                    except Exception as e:
                        print(e)
                else:
                    msg = '@{0} , you have no set an address yet'.format(author)
                    await client.say(msg)
                    print(author, " has not created an account yet")
            else:
                msg = 'Invalid address. Please enter a Poseidon address beginning with Q'
                await client.say(msg)
                print(author, " tried invalid NEW address")

        else:
            msg = 'Invalid address. Please enter a Poseidon address beginning with Q'
            await client.say(msg)
            print(author, " tried invalid NEW address")

@client.command(pass_context=True)
async def profile(ctx, message=None):

    if (message == None):
        conn = connect()
        author = ctx.message.author

        try:
            dbhandler = conn.cursor()
            checkdb = dbhandler.execute("SELECT address from test WHERE user_id = '{0}'".format(author))
            posqAddress = dbhandler.fetchone()

            if (checkdb): # USER HAS A DATABASE ENTRY
                dbhandler.execute("SELECT total from test WHERE user_id = '{0}'".format(author))
                posq = dbhandler.fetchone()
                msg = 'User = @{0} \nPOSQ address = {1} \nPOSQ CREDIT = {2}'.format(author, posqAddress[0], posq[0])
                await client.say(msg)
                print(author, "checked profile")

            else:
                msg = 'User {0} has not created a profile yet. use !help or !set'.format(author)
                print(author, " NO PROFILE EXIST")
                await client.say(msg)

        except Exception as e:
            print(e)
            msg = 'User {0} does not have a profile'.format(author)
            await client.say(msg)

    else:
        conn = connect()
        author = ctx.message.author

        try:
            dbhandler = conn.cursor()
            checkdb = dbhandler.execute("SELECT address from test WHERE id_number = '{0}'".format(message))
            posqAddress = dbhandler.fetchone()

            if (checkdb): # USER HAS A DATABASE ENTRY
                dbhandler.execute("SELECT total from test WHERE id_number = '{0}'".format(message))
                posq = dbhandler.fetchone()
                msg = 'User = {0} \nPOSQ address = {1} \nPOSQ CREDIT = {2}'.format(message, posqAddress[0], posq[0])
                await client.say(msg)
                print(author, " checked ", message, " profile")

            else:
                msg = 'User {0} has not created a profile yet. use !help or !set'.format(message)
                print(message, " NO PROFILE EXIST")
                await client.say(msg)

        except Exception as e:
            print(e)
            msg = 'User {0} does not have a profile'.format(author)
            await client.say(msg)
client.run(token)
