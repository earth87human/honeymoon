import codecs

with codecs.open('/Users/macuser/honeymoon/index.html', 'r', 'utf-8') as f:
    lines = f.readlines()

start_index = 1914 # 0-indexed for 1915
end_index = 2112 # 0-indexed for 2112
assert "<!-- Day 7 -->" in lines[start_index]
assert "</div>" in lines[end_index-1]

new_content_day7_8 = """                    <!-- Day 7 -->
                    <div class="accordion-item">
                        <div class="accordion-header">
                            <div class="accordion-day-badge">
                                <span class="day-num">7</span>
                                <span class="day-label">Day</span>
                            </div>
                            <div class="accordion-header-info">
                                <span class="date">3/22 (日)</span>
                                <h4>在地生活圈、無敵海景野餐與黃昏貢多拉</h4>
                                <div class="preview-tags">
                                    <span class="preview-tag">📸 聖馬可晨拍</span>
                                    <span class="preview-tag">🍷 海景野餐</span>
                                    <span class="preview-tag">🛶 黃昏貢多拉</span>
                                </div>
                            </div>
                            <div class="accordion-toggle">
                                <i class="fas fa-chevron-down"></i>
                            </div>
                        </div>
                        <div class="accordion-body">
                            <div class="accordion-body-inner">
                                <div class="activity-list">
                                    <div class="activity-item highlight">
                                        <div class="activity-time">
                                            <span class="time">07:00</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag hotel">🏨 晨間</span>
                                            <h5>晨間充電：飯店早餐與準備野餐包</h5>
                                            <p><strong>✨ 體驗：</strong>悠哉起床，在 Carnival Palace Hotel 吃頓豐盛早餐。出門前，把昨天在古蹟超市買好的義大利生火腿、起司與紅酒妥善裝進背包裡，準備開啟悠閒的一天。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time">
                                            <span class="time">08:30</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag sight">📸 拍照</span>
                                            <h5>獨享聖馬可的清晨 (Piazza San Marco)</h5>
                                            <p><strong>🚶 交通：</strong>步行約 30-35 分鐘。<br>
                                            <strong>✨ 體驗：</strong>一日遊大軍抵達前的黃金時刻。這時光線最柔和，廣場極度空曠，沒有白天的喧囂擁擠。請務必把握這個機會架上腳架，拍下兩人與大教堂、總督宮的完美空景合照，捕捉水都最純粹的靜謐美感。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item">
                                        <div class="activity-time">
                                            <span class="time">09:30</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag sight">🏛️ 景點</span>
                                            <h5>隱藏版建築奇觀：蝸牛塔 (Scala Contarini del Bovolo)</h5>
                                            <p><strong>🚶 交通：</strong>從聖馬可廣場鑽進小巷，步行約 5-8 分鐘。<br>
                                            <strong>✨ 體驗：</strong>藏在極深巷弄裡的 15 世紀建築奇蹟。「Bovolo」是威尼斯語的蝸牛，這座高達 28 公尺的紅磚螺旋樓梯，完美結合了文藝復興與拜占庭風格。沿著優雅的迴旋樓梯爬到頂端，從一個極其特別的視角俯瞰威尼斯的紅磚屋頂與鐘樓。一般遊客極少知道這個秘境！</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time">
                                            <span class="time">11:00</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag food">☕ 早茶</span>
                                            <h5>在地人私藏的糕點神店：Pasticceria Toletta</h5>
                                            <p><strong>🚶 交通：</strong>跨過木造學院橋來到多爾索杜羅區 (Dorsoduro)，步行約 15 分鐘。<br>
                                            <strong>✨ 體驗：</strong>這家店幾乎沒有座位，大家都是「站著」吃！跟著當地居民擠在玻璃櫃前，點一杯極具水準的卡布奇諾，配上他們家超級出名的千層酥或是口感鬆軟的義式可頌 (Cornetto)。用幾歐元的親民價格，享受最道地、評價極高的義式早茶時光。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time">
                                            <span class="time">12:30</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag food">🍷 野餐</span>
                                            <h5>舒服的無敵海景野餐 (Fondamenta delle Zattere)</h5>
                                            <p><strong>🚶 交通：</strong>喝完咖啡往南漫步走到 Zattere 海岸步道，大約 5-8 分鐘。<br>
                                            <strong>🍴 體驗：</strong>拿出背包裡準備好的超市美食！這條步道面對著朱代卡水道，沿岸有許多木造長椅和寬闊平坦的石階，是威尼斯極少數可以合法、舒服坐下來吃東西的地方。一邊吹著海風看著大船入港，一邊享用專屬你們的蜜月午餐，享受不被打擾的兩人時光。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item">
                                        <div class="activity-time">
                                            <span class="time">14:30</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag sight">⛪ 景點</span>
                                            <h5>壯麗的圓頂地標：安康聖母大教堂 (Basilica della Salute)</h5>
                                            <p><strong>🚶 交通：</strong>吃飽後，沿著 Zattere 步道一路往東邊（左手邊）走到底，轉個彎就會抵達，全程平坦步行約 10-15 分鐘。<br>
                                            <strong>✨ 體驗：</strong>走進這座宏偉的八角形教堂。這是當年為了慶祝黑死病結束而建，內部空間極其壯觀，光線從巨大的穹頂灑下，給人一種非常神聖平靜的感覺，與聖馬可大教堂的華麗截然不同。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item">
                                        <div class="activity-time">
                                            <span class="time">15:30</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag sight">🚶 散步</span>
                                            <h5>水巷迷宮的午後漫步</h5>
                                            <p><strong>🚶 交通：</strong>從教堂離開後，慢慢往北朝著 San Polo 區或 Cannaregio 區的方向悠遊漫步。<br>
                                            <strong>✨ 體驗：</strong>下午沒有任何趕場壓力。牽著手在多爾索杜羅區充滿藝術氣息的小巷裡悠哉迷路，看看櫥窗裡的玻璃藝品手作小店，享受兩人專屬的威尼斯街景。迷路，就是體驗威尼斯最好的方式。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time">
                                            <span class="time">17:30</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag activity">🛶 體驗</span>
                                            <h5>蜜月高光時刻：黃昏貢多拉體驗 (Gondola)</h5>
                                            <p><strong>🚶 交通：</strong>在漫步回飯店的途中，經過相對安靜的水道（如 San Polo 區）時，直接找船夫包船。<br>
                                            <strong>✨ 體驗：</strong>把握「魔幻時刻 (Magic Hour)」！捨棄擁擠的大運河，讓船夫帶你們穿梭在寧靜狹窄的磚牆水巷中。看著夕陽把水面和橋樑染成橘金色，聽著水波拍打船身的聲音，體驗水都最極致的浪漫。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time">
                                            <span class="time">18:30</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag food">🍝 晚餐</span>
                                            <h5>週日限定晚餐：Trattoria Bar Pontini</h5>
                                            <p><strong>🚶 交通：</strong>貢多拉下船後，步行回到飯店所在的 Cannaregio 區。<br>
                                            <strong>🍴 體驗：</strong>因為它星期一公休，今晚是唯一機會！找個位子坐下來，點一盤熱騰騰、海鮮滿出來的義大利麵 (Spaghetti allo Scoglio) 或是特色的墨魚麵，犒賞一整天的步伐。這家極受當地人與遊客歡迎，份量十足又美味。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item">
                                        <div class="activity-time">
                                            <span class="time">20:30</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag hotel">🚶 散步</span>
                                            <h5>漫步回飯店休息</h5>
                                            <p>吃飽喝足後，吹著夜晚微涼的風，沿著運河悠哉漫步回 Carnival Palace Hotel，為充實浪漫的 Day 7 畫下完美句點。</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Day 8 -->
                    <div class="accordion-item">
                        <div class="accordion-header">
                            <div class="accordion-day-badge">
                                <span class="day-num">8</span>
                                <span class="day-label">Day</span>
                            </div>
                            <div class="accordion-header-info">
                                <span class="date">3/23 (一)</span>
                                <h4>市場尋寶、帝國古蹟與弦樂之夜</h4>
                                <div class="preview-tags">
                                    <span class="preview-tag">🐟 里亞托市場</span>
                                    <span class="preview-tag">🏛️ 總督宮</span>
                                    <span class="preview-tag">🎻 弦樂音樂會</span>
                                </div>
                            </div>
                            <div class="accordion-toggle">
                                <i class="fas fa-chevron-down"></i>
                            </div>
                        </div>
                        <div class="accordion-body">
                            <div class="accordion-body-inner">
                                <div class="activity-list">
                                    <div class="activity-item">
                                        <div class="activity-time">
                                            <span class="time">07:00</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag hotel">🏨 晨間</span>
                                            <h5>晨間時光：飯店早餐</h5>
                                            <p>悠哉起床，在飯店舒舒服服地吃頓豐盛早餐，儲備今日探索歷史建築的體力。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time">
                                            <span class="time">08:30</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag sight">🐟 景點</span>
                                            <h5>走進威尼斯人的大廚房：里亞托市場 (Mercato di Rialto)</h5>
                                            <p><strong>🚶 交通：</strong>步行約 20 分鐘。<br>
                                            <strong>✨ 體驗：</strong>星期一早上市場最有活力！看當地老奶奶和餐廳主廚在鮮花與海鮮攤位前穿梭，叫賣聲此起彼落，感受幾百年來未曾改變的商業運作日常。一定要看看攤位上那些奇形怪狀的亞得里亞海新鮮漁獲。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time">
                                            <span class="time">10:00</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag food">🍷 小吃</span>
                                            <h5>最新鮮的市場小吃 (All'Arco)</h5>
                                            <p><strong>🚶 交通：</strong>從市場步行約 2 分鐘。<br>
                                            <strong>🍴 體驗：</strong>就在市場旁邊的巷子內。點幾份鋪著甜蝦、小章魚或奶油鱈魚泥的小食 (Crostini)，學威尼斯人站在小巷裡當作早午餐大快朵頤，海鮮的甘甜搭配略帶咬勁的麵包，美味絕倫。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item">
                                        <div class="activity-time">
                                            <span class="time">12:15</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag sight">🌇 觀景</span>
                                            <h5>俯瞰水都全景 (T Fondaco dei Tedeschi)</h5>
                                            <p><strong>🚶 交通：</strong>跨過里亞托橋，步行約 5 分鐘。<br>
                                            <strong>✨ 體驗：</strong>這是由古蹟（昔日的德國商館）改建的奢華精品百貨。搭電梯直達頂樓的免費觀景台（💡 <strong>強烈提醒：務必提前於官網預約</strong>），站在最高點 360 度俯瞰大運河壯麗的 S 型彎道與綿延的紅磚屋頂，是威尼斯最值回票價(免費!)的視角。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time">
                                            <span class="time">13:30</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag sight">✨ 景點</span>
                                            <h5>聖馬可大教堂 (Basilica di San Marco)</h5>
                                            <p><strong>🚶 交通：</strong>步行約 10 分鐘。<br>
                                            <strong>✨ 體驗：</strong>下午的光線剛好能把教堂內部純金箔鑲嵌的穹頂照得閃閃發光！感受拜占庭風格的強烈視覺衝擊，以及威尼斯作為東西方文明交匯點的歷史痕跡。牆上精美的馬賽克壁畫訴說著聖經故事與聖馬可遺骨的傳奇。（💡 <strong>建議先在官網預約門票免排隊</strong>）</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time">
                                            <span class="time">14:30</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag sight">🏛️ 景點</span>
                                            <h5>總督宮 (Palazzo Ducale) 與嘆息橋內部</h5>
                                            <p><strong>🚶 交通：</strong>步行約 1 分鐘（就在大教堂隔壁）。<br>
                                            <strong>✨ 體驗：</strong>穿過極度華麗、世界最大的無樑柱房間「大議會大廳」，親自走進嘆息橋內部，透過石縫網格體會當年囚犯看威尼斯最後一眼的真實絕望感受。這裡不僅是壯觀的總督官邸，更是觀察威尼斯共和國如何透過嚴密的社會結構與審判制度，維持其海權文明長達數百年的絕佳歷史見證。（💡 <strong>建議先在官網預約門票，省去大排長龍的時間</strong>）</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time">
                                            <span class="time">17:00</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag food">🍷 晚餐</span>
                                            <h5>造船廠的工匠日常與 Cicchetti 晚餐 (Osteria Al Squero)</h5>
                                            <p><strong>🚶 交通：</strong>離開廣場跨過木造學院橋，步行約 20 分鐘來到多爾索杜羅區。<br>
                                            <strong>🍴 體驗：</strong>把這裡直接當作今天的晚餐基地！來回多點幾輪便宜又好吃的小食（極度推薦黑松露火腿、鱈魚泥等口味），配上幾杯橘色 Spritz。坐在矮牆上親眼看著師傅敲敲打打修繕黑色木造貢多拉船，直到夕陽落下、工廠打烊，享受最愜意飽足的在地傍晚時光。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time">
                                            <span class="time">20:30</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag activity">🎻 體驗</span>
                                            <h5>夜間深度體驗：聖維陀教堂弦樂音樂會 (Interpreti Veneziani)</h5>
                                            <p><strong>🚶 交通：</strong>慢慢散步，跨回學院橋旁邊的聖維陀教堂 (Chiesa di San Vidal)，步行約 10 分鐘。（💡 <strong>務必提前在官網購票</strong>）<br>
                                            <strong>✨ 體驗：</strong>坐在這座古老教堂裡，不僅是聽覺享受，更能透過演奏者的忘情演出，近距離觀察純木造弦樂器的物理構造。留意這些古典提琴的琴橋設定與弦距如何影響共鳴與音色，同時感受韋瓦第《四季》中巴洛克時期的和弦進行與張力（這些樂理基礎其實與現代流行音樂發展息息相關！）。純粹的音階與和聲在教堂高聳的穹頂與大理石牆面間完美迴盪，展現了原聲樂器的極致魅力。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item">
                                        <div class="activity-time">
                                            <span class="time">22:00</span>
                                        </div>
                                        <div class="activity-content">
                                            <span class="activity-tag hotel">🧳 收尾</span>
                                            <h5>漫步回房與行李收尾</h5>
                                            <p><strong>🚶 交通：</strong>聽完音樂會後，趁著微涼的夜風牽手散步回飯店（約 25 分鐘），或是跳上一班夜間行駛的大運河水上巴士 (Vaporetto)，從水路欣賞靜謐的威尼斯夜景。<br>
                                            回房後將這三天的回憶與行李打包收尾，準備迎接明天的科莫湖仙境之旅。</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="accordion-tip">
                                    <strong><i class="fas fa-heart"></i> 威尼斯回憶</strong>
                                    <p>告別這座偉大的水城共和國！明天一早將出發前往阿爾卑斯山腳下的科莫湖 🏞️ 準備換上度假模式，五星級蜜月高潮即將展開！</p>
                                </div>
                            </div>
                        </div>
                    </div>
"""
lines[start_index:end_index] = [new_content_day7_8]

with codecs.open('/Users/macuser/honeymoon/index.html', 'w', 'utf-8') as f:
    f.writelines(lines)

