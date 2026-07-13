import discord
from discord import app_commands
import asyncio
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

active_wars = {}

# Hơn 300 dòng kiểu dân war
curse_messages = [
    "{user} speed em=))", "{user} six à con chó=))", "{user} cham a=))", "{user} bai cha ak=))",
    "{user} ngu vl=))", "{user} óc chó à=))", "{user} phế vl=))", "{user} cút mẹ mày đi=))",
    "{user} não úng à=))", "{user} con đĩ=))", "{user} loser ak=))", "{user} ngu như bò=))",
    "{user} đéo não hả=))", "{user} thằng phế=))", "{user} cặc à=))", "{user} mẹ mày chết chưa=))",
    "{user} vô dụng vl=))", "{user} bị block hết à=))", "{user} thảm hại ak=))", "{user} ngu kinh=))",
    "{user} rep lại coi=))", "{user} mặt dày vl=))", "{user} fail vl=))", "{user} óc bò=))",
    "{user} speed à con chó=))", "{user} six vl=))", "{user} cham ak=))", "{user} bai cha=))",
    "{user} ngu vcl=))", "{user} thằng ngu=))", "{user} phế vật ak=))", "{user} cút đi=))",
    "{user} não úng nước=))", "{user} con đĩ mẹ=))", "{user} loser vl=))", "{user} ngu vl luôn=))",
    "{user} đéo có não=))", "{user} thằng chó=))", "{user} cặc vl=))", "{user} mẹ mày=))",
    "{user} vô dụng ak=))", "{user} block hết=))", "{user} thảm hại vl=))", "{user} ngu vl=))",
] * 20   # Nhân lên thành hơn 300 dòng

@client.event
async def on_ready():
    await tree.sync()
    print(f'✅ Bot online - Tốc độ 0.1s!')

@tree.command(name="war", description="Bắt đầu war")
@app_commands.describe(user="Người muốn chửi")
async def war(interaction: discord.Interaction, user: discord.Member):
    if interaction.user.id in active_wars:
        await interaction.response.send_message("Đang war rồi, /stop trước!", ephemeral=True)
        return

    active_wars[interaction.user.id] = True
    await interaction.response.send_message(f"🚨 **WAR SIÊU TỐC 0.1s** với {user.mention} BẮT ĐẦU!!!", ephemeral=True)

    try:
        i = 0
        while active_wars.get(interaction.user.id, False):
            msg = curse_messages[i % len(curse_messages)]
            try:
                await interaction.channel.send(msg.format(user=user.mention))
            except:
                pass
            i += 1
            await asyncio.sleep(0.1)   # Siêu nhanh 0.1 giây
    except:
        pass
    finally:
        active_wars.pop(interaction.user.id, None)

@tree.command(name="stop", description="Dừng war")
async def stop(interaction: discord.Interaction):
    if interaction.user.id in active_wars:
        active_wars[interaction.user.id] = False
        await interaction.response.send_message("✅ Dừng war!", ephemeral=True)
    else:
        await interaction.response.send_message("Chưa war ai!", ephemeral=True)

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        print("❌ Thiếu DISCORD_TOKEN!")
    else:
        client.run(TOKEN)
