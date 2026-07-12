import discord
from discord import app_commands
import asyncio
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True   # Cần bật trong portal

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

active_wars = {}

curse_messages = [
    "Đm {user} mày là thằng ngu lồn!", "{user} con chó đẻ, cút mẹ mày đi!", 
    "Ê {user} lồn mẹ mày, não mày để đâu?", "{user} thằng phế vật, đồ óc chó!",
    "Đéo não hả {user} con đĩ?", "{user} mày là con cặc, mẹ mày chết chưa?",
    "Tao chửi mày đến chết {user} đồ ngu!", "{user} con đĩ mẹ, mày sống làm gì?",
    "{user} thằng bẩn thỉu, cút ra khỏi server!", "Mẹ kiếp {user}, mày là đồ vô dụng!",
    "{user} con lợn, não mày bằng phân!", "Đm {user} mày ngu như bò!",
    "{user} đồ đĩ, tao chửi mày 24/7!", "{user} mày là thằng loser!",
    "Lồn {user} ơi, mày có não không?", "{user} con đĩ ngựa!",
    "{user} mày chết đi cho rồi!", "Thằng {user} ngu vl!",
]

@client.event
async def on_ready():
    await tree.sync()
    print(f'✅ Bot {client.user} đã online thành công!')

@tree.command(name="war", description="Bắt đầu war")
@app_commands.describe(user="Người muốn chửi")
async def war(interaction: discord.Interaction, user: discord.Member):
    if interaction.user.id in active_wars:
        await interaction.response.send_message("Bạn đang war rồi!", ephemeral=True)
        return

    active_wars[interaction.user.id] = True
    await interaction.response.send_message(f"🚨 Đang WAR {user.mention}...", ephemeral=True)

    try:
        while active_wars.get(interaction.user.id, False):
            for msg in curse_messages:
                if not active_wars.get(interaction.user.id, False):
                    break
                try:
                    await interaction.channel.send(msg.format(user=user.mention))
                except:
                    pass
                await asyncio.sleep(0.35)
    except:
        pass
    finally:
        active_wars.pop(interaction.user.id, None)

@tree.command(name="stop", description="Dừng war")
async def stop(interaction: discord.Interaction):
    if interaction.user.id in active_wars:
        active_wars[interaction.user.id] = False
        await interaction.response.send_message("✅ Đã dừng war!", ephemeral=True)
    else:
        await interaction.response.send_message("Chưa war ai cả!", ephemeral=True)

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        print("❌ Thiếu DISCORD_TOKEN!")
    else:
        client.run(TOKEN)
