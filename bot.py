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

# 🔥 Danh sách câu chửi (rất nhiều + thô hơn)
curse_messages = [
    "Đm {user} mày là thằng ngu lồn!",
    "{user} con chó đẻ, cút mẹ mày đi!",
    "Ê {user} lồn mẹ mày, não mày để đâu?",
    "{user} thằng phế vật, đồ óc chó!",
    "Đéo não hả {user} con đĩ?",
    "{user} mày là con cặc, mẹ mày chết chưa?",
    "Tao chửi mày đến chết {user} đồ ngu!",
    "{user} con đĩ mẹ, mày sống làm gì?",
    "{user} thằng bẩn thỉu, cút ra khỏi server!",
    "Mẹ kiếp {user}, mày là đồ vô dụng!",
    "{user} con lợn, não mày bằng phân!",
    "Đm {user} mày ngu như bò, chả biết gì!",
    "{user} đồ đĩ, tao chửi mày 24/7!",
    "Con {user} này chỉ đáng bị chửi!",
    "{user} mày là thằng loser, cút mẹ đi!",
    "Lồn {user} ơi, mày có não không?",
    "{user} con đĩ ngựa, tao ghét mày!",
    "Đéo phải người {user}, là con vật!",
    "{user} mày chết đi cho rồi!",
    "Thằng {user} ngu vl, tao chửi mày hoài!",
]

@client.event
async def on_ready():
    await tree.sync()
    print(f'Bot {client.user} đã online và sẵn sàng war!')

@tree.command(name="war", description="Bắt đầu war người khác")
@app_commands.describe(user="Người bạn muốn chửi")
async def war(interaction: discord.Interaction, user: discord.Member):
    if interaction.user.id in active_wars:
        await interaction.response.send_message("Bạn đang war rồi! Dùng `/stop` trước.", ephemeral=True)
        return

    active_wars[interaction.user.id] = True
    await interaction.response.send_message(f"🚨 Đang **WAR** {user.mention} ngay bây giờ!", ephemeral=True)

    try:
        while active_wars.get(interaction.user.id, False):
            for msg in curse_messages:
                if not active_wars.get(interaction.user.id, False):
                    break
                try:
                    await interaction.channel.send(msg.format(user=user.mention))
                except:
                    try:
                        await user.send(msg.format(user
