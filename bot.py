import discord
from discord.ext import commands

client = discord.Client()

token = "OTEyNTIxNjY0OTU1MzE0MjE2.YZxKBg.Va-jCT5LmHjcRw4OJrNgsZZokrw"

bad = ["시발", "ㅅㅂ", "tlqkf", "느금"]


@client.event
async def on_ready():
    print(client.user.name)
    print("봇 준비 완료!")
    game = discord.Game("테스트")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    if message.content == "야":
        await message.channel.send("ㅎㅇ")
    if message.content == "!앙":
        await message.channel.send("기모링")
    mc = message.content
    for i in bad:
        if i in mc:
            await message.channel.send(f"{message.author.mention}님이 욕을 하셨습니다.")
            await message.delete()
    if message.content == "엄준식":
        embed = discord.Embed(color=discord.Colour.magenta(), title="엄준식", description="[원본](https://www.google.com/url?sa=i&url=https%3A%2F%2Ftalk.op.gg%2Fs%2Flol%2Ffree%2F2250255%2F%25EC%2597%2584%25EC%25A4%2580%25EC%258B%259D-%25EA%25B3%25A0%25ED%2599%2594%25EC%25A7%2588&psig=AOvVaw3SyDKTyWi0Ha7gb4zdNuSB&ust=1637720456131000&source=images&cd=vfe&ved=0CAgQjRxqFwoTCPCfw6O2rfQCFQAAAAAdAAAAABAD)")
        embed.add_field(name="필드", value="필드 내용", inline=False)
        embed.set_image(
            url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA5MDFfMjgz%2FMDAxNTk4OTU3ODU5MDY3.olgPBCGRdx7M9urWK3vN8dlMh3BQSIM2AFjQQYFktwMg.OwlZSD_28vvcBIzu8HljBKDuVeoCszAOKiVEKm4hc7gg.JPEG.zinc1019%2F1598957858095.jpeg&type=sc960_832")
        embed.set_thumbnail(
            url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA5MDFfMjgz%2FMDAxNTk4OTU3ODU5MDY3.olgPBCGRdx7M9urWK3vN8dlMh3BQSIM2AFjQQYFktwMg.OwlZSD_28vvcBIzu8HljBKDuVeoCszAOKiVEKm4hc7gg.JPEG.zinc1019%2F1598957858095.jpeg&type=sc960_832")
        await message.channel.send(embed=embed)
    if message.content.startswith("!청소"):
        number = int(message.content.split()[1])
        await message.channel.purge(limit=number + 1)
        await message.channel.send(f"{number}개 메세지 삭제완료!")
    if message.content == "!help":
        embed = discord.Embed(color=discord.Colour.blue(), title="Plugins Commands", description="!help command")

        await message.channel.send(embed=embed)


client.run(token)