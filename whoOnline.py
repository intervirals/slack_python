from slacker import Slacker

slack = Slacker('xoxp-70997678455-71005628514-71312901170-f87b8ff08c') #intervirals_testing slack token generated

# Send a message to #general channel
slack.chat.post_message('#general', 'Hello fellow slackersssss :D!')

# Get users list
response = slack.users.list()
users = response.body['members']

# Upload a file
slack.files.upload('hello.txt')
