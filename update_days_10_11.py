import codecs

# Define the "EXTREME DETAIL" content for Day 10 and Day 11
# This string replaces everything between <!-- Day 10 --> and <!-- Stage 5: Milan -->
new_day10_11 = """                    <!-- Day 10 -->
                    <div class="accordion-item">
                        <div class="accordion-header">
                            <div class="accordion-day-badge">
                                <span class="day-num">10</span>
                                <span class="day-label">Day</span>
                            </div>
                            <div class="accordion-header-info">
                                <span class="date">3/25 (三)</span>
                                <h4>⛴️ 水上科莫——豪華自駕與黃金三角</h4>
                                <div class="preview-tags">
                                    <span class="preview-tag">🚢 貝拉焦</span>
                                    <span class="preview-tag">🚤 豪華自駕</span>
                                    <span class="preview-tag">🏛️ 莫納斯特羅別墅</span>
                                </div>
                            </div>
                            <div class="accordion-toggle">
                                <i class="fas fa-chevron-down"></i>
                            </div>
                        </div>
                        <div class="accordion-body">
                            <div class="accordion-body-inner">
                                <div class="day-intro">
                                    <h5><i class="fas fa-ship"></i> 掌握湖心：從水路拆解兩千年的奢華</h5>
                                    <p>這天的核心是「水路」。你將掌握方向盤，從湖心視角拆解這座兩千年來讓歐洲權貴瘋狂的湖泊，體驗絕對的自由與電影質感。</p>
                                </div>
                                <div class="activity-list">
                                    <div class="activity-item highlight">
                                        <div class="activity-time"><span class="time">07:00</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag food">🍳 早餐</span>
                                            <h5>07:00 - 09:00 | 晨光序幕：五星級能量補給</h5>
                                            <p>地點：<a href="https://maps.app.goo.gl/uXv7wW4R5L2vN4kPA" target="_blank">Grand Hotel Victoria 景觀餐廳</a>。<br>
                                            ① <strong>深度早餐：</strong>坐在窗邊，看著晨霧中的 Bellagio 慢慢甦醒。<br>
                                            ② <strong>物資整備：</strong>離開前去 SPA 中心借 2 條大毛巾。自駕船時湖風大，可用來防風或墊在甲板上野餐，非常關鍵。<br>
                                            ③ <strong>APP 準備：</strong>下載 Google Maps 離線地圖，確保你在湖心定位精準。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item">
                                        <div class="activity-time"><span class="time">09:00</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag sight">📸 探索</span>
                                            <h5>09:00 - 12:00 | 貝拉焦 (Bellagio)：湖中之珠深度探索</h5>
                                            <p>交通：08:30 從 Menaggio 碼頭搭乘渡輪，約 15 分鐘抵達。<br><br>
                                            ① <strong><a href="https://www.google.com/maps/search/Salita+Serbelloni+Bellagio" target="_blank">Salita Serbelloni（老街攝影）</a></strong>：這條街是科莫湖的「臉面」。趁觀光大軍尚未抵達，拍下最純粹的斜陽與階梯。<br>
                                            ② <strong><a href="https://www.google.com/maps/search/Villa+Melzi+Bellagio" target="_blank">Villa Melzi（梅爾齊別墅）</a></strong>：漫步於臨水的林蔭大道，尋找那座摩爾式藍頂涼亭，感受義大利貴族對東方美學的想像。<br>
                                            ③ <strong>關鍵行動 (物資採買)：</strong>前往鎮上的熟食店 Salumeria 購買現做 Panini（推薦義大利生火腿 Prosciutto 配 Mozzarella）與氣泡水。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time"><span class="time">12:00</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag activity">🚤 重頭戲</span>
                                            <h5>12:00 - 15:00 | 重頭戲：3 小時豪華遊艇自駕（三大經典點）</h5>
                                            <p>起點：Bellagio 東側的 <a href="https://www.google.com/maps/search/Pescallo+Bay+Bellagio" target="_blank">Pescallo 灣</a> 取船。<br>
                                            <strong>操作邏輯：</strong>往前推 Go，拉回中央 Idle，往後 Reverse。左手控制方向盤，邏輯簡單且穩定性高。<br><br>
                                            📍 <strong>第一站：<a href="https://www.google.com/maps/search/Villa+del+Balbianello" target="_blank">Villa del Balbianello (星戰別墅)</a></strong><br>
                                            關小油門，慢速繞行半島。從湖心仰望那個三拱廊 (Loggia)。這是你 Day 11 會步行的終點，先從湖上預習它的壯闊。<br><br>
                                            📍 <strong>第二站：<a href="https://www.google.com/maps/search/Orrido+di+Nesso" target="_blank">Orrido di Nesso (隱藏瀑布與羅馬古橋)</a></strong><br>
                                            跨越湖泊往對岸 Nesso。你會看到古老的 <a href="https://www.google.com/maps/search/Ponte+della+Civera+Nesso" target="_blank">羅馬石拱橋</a> 跨越峽谷。關掉引擎，聽瀑布轟鳴在山谷回盪。<br><br>
                                            📍 <strong>第三站：<a href="https://www.google.com/maps/search/Tremezzo+Lake+Como" target="_blank">Tremezzo 黃金海岸 (下錨野餐)</a></strong><br>
                                            這裡是下錨野餐的最佳地點。拿出早上的帕尼尼，披上飯店毛巾。享受整趟蜜月最放鬆的 30 分鐘——沒有遊客，只有山、水和你們。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item">
                                        <div class="activity-time"><span class="time">15:30</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag sight">🚶 情懷</span>
                                            <h5>15:30 - 17:30 | 瓦倫納 (Varenna)：漁村情懷</h5>
                                            <p>交通：歸還船隻後，搭渡輪前往 Varenna (約 20 分鐘)。<br>
                                            ① <strong><a href="https://www.google.com/maps/search/Passerella+degli+Innamorati+Varenna" target="_blank">Passerella degli Innamorati（情人步道）</a></strong>：懸掛在岩壁上的紅色步道，感受漁村與湖水零距離接觸。<br>
                                            ② <strong><a href="https://www.google.com/maps/search/Villa+Monastero+Varenna" target="_blank">Villa Monastero（莫納斯特羅別墅）</a></strong>：視覺重點在「羅馬廊柱」（Loggia），那是整座湖最完美的相框。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item">
                                        <div class="activity-time"><span class="time">17:30</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag activity">🧖 救贖</span>
                                            <h5>17:30 - 20:30 | 回航與救贖：SPA 的溫柔</h5>
                                            <p>回程：17:30 搭渡輪回 Menaggio。此時日落會將雪山染成粉紫色。<br>
                                            <strong>ERRE Spa (第 2 次)：</strong>針對湖上 3 小時被湖風帶走的體溫進行「性能優化」。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time"><span class="time">20:30</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag food">🍷 晚宴</span>
                                            <h5>20:30+ | 晚宴：Bar Manzoni 古典晚宴</h5>
                                            <p>梳洗後換上這趟旅行最優雅的晚裝，走進歷史主棟的 Bar Manzoni。這是飯店最有氣氛的酒吧，由 Bar Manager <strong>Alessandro Lippo</strong> 操刀設計 Signature Cocktails，把這裡當作今晚的正式晚餐。</p>

                                            <div style="background: #1a1a2e; border-radius: 12px; padding: 1.2rem; margin: 1rem 0; color: #eee;">
                                                <h6 style="margin-top:0; color: #f39c12; border-bottom: 2px solid #f39c12; padding-bottom: 0.5rem;">📋 Bar Manzoni 完整菜單</h6>
                                                
                                                <p style="margin: 0.8rem 0 0.3rem; font-weight: bold; color: #f39c12;">🍸 SIGNATURE COCKTAILS (每杯 €30)</p>
                                                <p style="font-size: 0.9em; margin: 0; color: #ddd;">
                                                • ⭐ <strong>CAFFÈ VILLA</strong>: Bourbon, 咖啡浸漬, 苦味糖漿 <em style="color:#f39c12;">← 男士首選</em><br>
                                                • <strong>LARIO SPICE</strong>: Como Gin, Chili, 番茄水, 熱情果<br>
                                                • ⭐ <strong>PEAK 51</strong>: Tequila, Mezcal, 特調柑橘醬 <em style="color:#f39c12;">← 珠峰探險致敬款</em><br>
                                                • <strong>SERRA 9</strong>: Gin, 萊姆, 薄荷, 夏日香氛</p>

                                                <p style="margin: 1.2rem 0 0.3rem; font-weight: bold; color: #f39c12;">🥃 烈酒選集 (Selected Spirits)</p>
                                                <p style="font-size: 0.9em; margin: 0; color: #bbb;">
                                                • <strong>SCOTCH:</strong> Macallan 12y €30 | ⭐ Lagavulin 16y €35 | Oban 14y €30<br>
                                                • <strong>BOURBON:</strong> Buffalo Trace €25 | ⭐ Eagle Rare 10y €32<br>
                                                • <strong>GIN & MORE:</strong> Hendrick's €27 | ⭐ Monkey 47 €30 | R Collection Como €25</p>

                                                <p style="margin: 1.2rem 0 0.3rem; font-weight: bold; color: #f39c12;">🍴 經典輕食與披薩 (€28-38)</p>
                                                <p style="font-size: 0.9em; margin: 0; color: #ddd;">
                                                • ⭐ <strong>Tagliere di salumi</strong>: 頂級冷肉起司拼盤 — <strong>€38</strong><br>
                                                • ⭐ <strong>Hamburger di Fassona</strong>: 皮埃蒙特牛肉漢堡 — <strong>€38</strong><br>
                                                • <strong>Pizza Saporita</strong>: 莫札瑞拉、鯷魚、酸山菜 — <strong>€36</strong><br>
                                                • ⭐ <strong>Tiramisù</strong>: Manzoni 限定版 — <strong>€24</strong></p>

                                                <p style="margin: 1.5rem 0 0.5rem; font-weight: bold; color: #f1c40f; border-top: 1px solid #444; padding-top: 1rem;">🍴 推薦點法建議 (Recommendations)</p>
                                                <p style="font-size: 0.9em; margin: 0; line-height: 1.6; color: #ddd;">
                                                <strong style="color:#fff;">🥃 點法 A：經典微醺（兩人約 €120）</strong><br>
                                                → 兩杯 ⭐ <strong>Signature Cocktails €60</strong> + ⭐ <strong>Pizza Saporita €36</strong> + ⭐ <strong>Tiramisù €24</strong><br><br>

                                                <strong style="color:#fff;">🍔 點法 B：飽腹首選（兩人約 €130）</strong><br>
                                                → 兩杯啤酒/軟飲 <strong>€30</strong> + ⭐ <strong>Fassona 漢堡 €38</strong> + ⭐ <strong>Tiramisù €24</strong><br><br>

                                                <strong style="color:#fff;">🍾 點法 C：極致浪漫（兩人約 €180）</strong><br>
                                                → ⭐ <strong>Cà del Bosco 一瓶 €85</strong> + ⭐ <strong>冷肉拼盤 €38</strong> + ⭐ <strong>Tiramisù €24</strong></p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="accordion-tip">
                                    <strong><i class="fas fa-coins"></i> Day 10 實用資費參考 (2人)</strong>
                                    <p>• 渡輪中湖一日券 (Day Pass)：€15 x 2 = €30<br>
                                    • 別墅門票 (Melzi + Monastero)：約 €25 x 2 = €50<br>
                                    • 3HR 遊艇租賃 (含燃料)：約 €450 - €600<br>
                                    • 輕食、Gelato 與下午茶：約 €40 - €60<br>
                                    • Bar Manzoni 晚餐預算：約 €120 - €160</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Day 11 -->
                    <div class="accordion-item">
                        <div class="accordion-header">
                            <div class="accordion-day-badge">
                                <span class="day-num">11</span>
                                <span class="day-label">Day</span>
                            </div>
                            <div class="accordion-header-info">
                                <span class="date">3/26 (四)</span>
                                <h4>🏍️ 山谷農莊與星戰別墅深度漫遊</h4>
                                <div class="preview-tags">
                                    <span class="preview-tag">🛵 飆風山道</span>
                                    <span class="preview-tag">🥩 農莊午餐</span>
                                    <span class="preview-tag">🎬 星戰別墅</span>
                                </div>
                            </div>
                            <div class="accordion-toggle">
                                <i class="fas fa-chevron-down"></i>
                            </div>
                        </div>
                        <div class="accordion-body">
                            <div class="accordion-body-inner">
                                <div class="day-intro">
                                    <h5><i class="fas fa-motorcycle"></i> 陸路秘境：深入山谷與電影場景</h5>
                                    <p>今天的主題是「自由」。將南下的體力轉移到「森林漫步」與「別墅停留」，深度感受電影場景的魅力。</p>
                                </div>
                                <div class="activity-list">
                                    <div class="activity-item highlight">
                                        <div class="activity-time"><span class="time">07:00</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag food">🍳 早餐</span>
                                            <h5>戰力補給</h5>
                                            <p>飯店悠哉早餐。既然今天要挑戰森林步道，早餐可以吃得更紮實一點。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time"><span class="time">09:00</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag activity">🛵 取車</span>
                                            <h5>準時取車</h5>
                                            <p>梅納焦廣場租車行報到。<strong>📋 SOP：</strong>檢查煞車、錄影巡車、確認油箱。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time"><span class="time">09:30</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag activity">🏍️ 騎行</span>
                                            <h5>上帝視角</h5>
                                            <p>導航 Plesio。直接往山上飆，在海拔 600 公尺處看湖景。這段路純騎車不走路，幫老婆拍幾張高山湖泊大片。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item">
                                        <div class="activity-time"><span class="time">11:30</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag activity">☕ 放空</span>
                                            <h5>農莊放空</h5>
                                            <p>抵達 Agriturismo Barcola。坐在戶外聽溪水聲看山谷發呆，享受餐前的安靜。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time"><span class="time">12:30</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag food">🥩 午餐</span>
                                            <h5>靈魂午餐</h5>
                                            <p>農莊大餐：手工玉米糕 (Polenta)、慢燉肉。這餐慢慢享用，預計 14:15 離開。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time"><span class="time">14:45</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag activity">🚶 漫步</span>
                                            <h5>森林漫步</h5>
                                            <p>騎車抵達 Lenno 停車場 (Lido di Lenno)。<br><br>
                                            ① <strong>步行進場：</strong>走進往別墅的森林步道 (Percorso Pedonale)。<br>
                                            ② <strong>⏱️ 體感：</strong>單程約 20-25 分鐘。這是一段優美的緩坡碎石路，能慢慢看見別墅隱現。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time"><span class="time">15:15</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag sight">🎬 景點</span>
                                            <h5>星戰別墅</h5>
                                            <p>深度探索 Villa del Balbianello。<br><br>
                                            <strong>📸 重點：</strong>在此待到滿意為止。這裡是安納金與艾米達拉祕密結婚的地點，光影極美。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item">
                                        <div class="activity-time"><span class="time">17:15</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag activity">🚶 回程</span>
                                            <h5>森林回程</h5>
                                            <p>沿原路散步回停車場。這時森林的光影非常有氛圍。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item">
                                        <div class="activity-time"><span class="time">17:45</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag activity">🏁 還車</span>
                                            <h5>北上還車</h5>
                                            <p>騎機車直接回梅納焦。還完車在碼頭邊看最後的夕陽。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time"><span class="time">18:30</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag activity">🧖 水療</span>
                                            <h5>終極 SPA</h5>
                                            <p>ERRE Spa (第 4 次)。完美救勢今日的疲勞。</p>
                                        </div>
                                    </div>
                                    <div class="activity-item highlight">
                                        <div class="activity-time"><span class="time">20:30</span></div>
                                        <div class="activity-content">
                                            <span class="activity-tag food">🍝 晚餐</span>
                                            <h5>在地餐館</h5>
                                            <p>步行至 Hosteria de Menàs，享受在地美味。</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="accordion-tip">
                                    <strong><i class="fas fa-lightbulb"></i> 執行細節與防雷提示</strong>
                                    <p>• <strong>步行的準備：</strong>建議穿好走的鞋子。<br>
                                    • <strong>別墅停留：</strong>Villa del Balbianello 的花園非常大，建議深度探索。<br>
                                    • <strong>機車裝備：</strong>山區防風外套與圍巾務必帶上。<br>
                                    • <strong>預約回顧：</strong>再次確認農莊預約。</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

with codecs.open('/Users/macuser/honeymoon/index.html', 'r', 'utf-8') as f:
    lines = f.readlines()

target_start = -1
target_end = -1
for i, line in enumerate(lines):
    # Strictly find the marker in the itinerary section
    if "<!-- Day 10 -->" in line:
         # To be safe, we only take the one that is far down the file (main itinerary)
         if i > 2000:
            target_start = i
            
    # ONLY search for Milan AFTER finding Day 10
    if target_start != -1 and "<!-- Stage 5: Milan -->" in line:
        target_end = i
        break

if target_start != -1 and target_end != -1:
    lines[target_start:target_end] = [new_day10_11 + "\n"]
    with codecs.open('/Users/macuser/honeymoon/index.html', 'w', 'utf-8') as f:
        f.writelines(lines)
    print(f"Successfully restored Bar Manzoni menu and recommendations.")
else:
    print(f"FAILED: target_start={target_start}, target_end={target_end}")
