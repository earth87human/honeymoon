import re

with open('/Users/macuser/honeymoon/index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

content = orig

# 1. 
content = content.replace('Casa Faccioli・肉醬寬麵', 'Casa Nina・肉醬寬麵')
# 2.
content = content.replace('住宿：Casa Faccioli Luxury B&B', '住宿：Casa Nina Bologna Centro')
# 3.
content = content.replace('入住 Casa Faccioli\n                                                    Luxury B&B', '入住 Casa Nina\n                                                    Bologna Centro')
# 4.
old_intro = """<p><strong>📜 住宿介紹：</strong>Casa Faccioli 是一間極高評價的精品 B&B，位於市中心絕對蛋黃區
                                                <strong>Via Caduti di Cefalonia</strong>，就在波隆那地標「雙塔 (Due
                                                Torri)」幾步路外的距離。這棟歷史建築經過精心翻修，保留了原始的木樑天花板與實木地板，結合現代舒適設施。<br>
                                                <strong>🏗️ 房間設施：</strong>
                                            <ul style="margin-top: 5px; list-style-type: circle; padding-left: 20px;">
                                                <li><strong>Espresso 咖啡機 & 電熱水壺：</strong>可以自己泡咖啡或茶，非常適合早餐 DIY。</li>
                                                <li><strong>小冰箱：</strong>可以冷藏在草市買的 Squacquerone 軟起司與水果。</li>
                                                <li><strong>頂級寢具：</strong>枕頭選單 (Pillow Menu)、羽絨被、隔音窗。</li>
                                                <li><strong>獨立衛浴：</strong>淋浴間、吹風機、高級沐浴用品。</li>
                                                <li><strong>免費高速 Wi-Fi</strong>、平面電視、空調。</li>
                                            </ul>
                                            <strong>✨ 入住：</strong>推開木門，放好沉重的行李。稍微確認一下房內提供的小餐具（盤子、叉子、酒杯），因為這將是晚上 Osteria"""

new_intro = """<p><strong>📜 住宿介紹：</strong>Casa Nina Bologna Centro 是一間極高評價的精品住宿，位於市中心絕對蛋黃區
                                                <strong>Via Oleari 4</strong>，距離波隆那心臟 Piazza Maggiore 僅約 50 公尺，周邊就是 Quadrilatero 美食街區與 Via Indipendenza 主幹道。完美的地理位置讓所有景點和美食都在步行範圍內。<br>
                                                <strong>🏗️ 房間設施：</strong>
                                            <ul style="margin-top: 5px; list-style-type: circle; padding-left: 20px;">
                                                <li><strong>咖啡機 & 電熱水壺：</strong>可以自己泡咖啡或茶，非常適合早餐 DIY。</li>
                                                <li><strong>小冰箱：</strong>可以冷藏在草市買的 Squacquerone 軟起司與水果。</li>
                                                <li><strong>舒適寢具：</strong>高品質床墊與枕頭、隔音窗。</li>
                                                <li><strong>獨立衛浴：</strong>淋浴間、吹風機、沐浴用品。</li>
                                                <li><strong>免費高速 Wi-Fi</strong>、空調。</li>
                                            </ul>
                                            <strong>✨ 入住：</strong>推開門，放好沉重的行李。稍微確認一下房內提供的小餐具（盤子、叉子、酒杯），因為這將是晚上 Osteria"""
content = content.replace(old_intro, new_intro)

# 5. links
content = content.replace('href="https://maps.google.com/?q=Casa+Faccioli+Bologna"', 'href="https://maps.google.com/?q=Casa+Nina+Bologna+Centro"')

# 6.
content = content.replace('就在您住的 Via\n                                                Caduti di Cefalonia 旁邊', '就在您住的 Via\n                                                Oleari 附近')
content = content.replace('就在您住的 Via Caduti di Cefalonia 旁邊', '就在您住的 Via Oleari 附近')

# 7.
content = content.replace('Casa Faccioli\n                                                B&B。把今天', 'Casa Nina。把今天')

# 8.
content = content.replace('Casa Faccioli 所在的區域', 'Casa Nina 所在的區域')

# 9.
content = content.replace('回到 Casa Faccioli。', '回到 Casa Nina。')

# 10.
content = content.replace('地理位置極無敵的 Casa Faccioli。', '地理位置極無敵的 Casa Nina。')
content = content.replace('將復古的鑰匙', '將鑰匙')

# 11.
content = content.replace('Casa Faccioli (3晚)', 'Casa Nina (3晚)')

# 12. Fix the link for Casa Nina Luxury B&B in one place that was weirdly split
content = content.replace('href="https://maps.google.com/?q=Casa+Faccioli+Luxury+B%26B+Bologna"', 'href="https://maps.google.com/?q=Casa+Nina+Bologna+Centro"')

if content != orig:
    with open('/Users/macuser/honeymoon/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replacements completed successfully!")
else:
    print("No changes were made. Script did not match.")
