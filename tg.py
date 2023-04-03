from shortzy import Shortzy

SHA = "1ec8439a6486baee17246d307963ce8f3e57820e"
SHW = "streaming.tamizhmasters.com"

async def get_shortlink(url):
        shortzy = Shortzy(SHA, SHW)
        return await shortzy.convert(url)
