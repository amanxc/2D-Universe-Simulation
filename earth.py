import pygame
import random
import math
import time
import copy

pygame.init()

WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Evren Simülasyonu - Gelişmiş Bilinçli Varlıklar")

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
CYAN = (0, 255, 255)
BROWN = (139, 69, 19)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)

CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 350

clock = pygame.time.Clock()

class Food:
    """Simülasyondaki yiyecek nesnelerini temsil eder."""
    def __init__(self, x, y, energy_value=20):
        self.x = x
        self.y = y
        self.size = 5
        self.color = GREEN
        self.energy_value = energy_value

    def draw(self, screen):
        """Yiyeceği ekranda çizer."""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)


class AdvancedConsciousness:
    """Gelişmiş bilinç sistemi - gerçek bilinç benzeri özellikler."""

    def __init__(self):
        # Bilinç katmanları
        self.attention_focus = None  # Neye odaklanıyor
        self.working_memory = []  # Aktif bellekte tutulan bilgiler
        self.episodic_memory = []  # Yaşanan deneyimler uzun süreli bellek
        self.semantic_memory = {}  # Kavramsal bilgi uzun süreli bellek
        # Meta-biliş düşünce hakkında düşünme
        self.metacognition = {
            'self_monitoring': random.uniform(0.1, 0.8),  # Kendi düşünce sürecini izleme
            'cognitive_control': random.uniform(0.1, 0.8),  # Bilişsel süreçleri kontrol etme
            'self_reflection': random.uniform(0.1, 0.8)  # Öz-yansıtma
        }

        # İç ses / düşünce akışı
        self.inner_voice = []  # İç sesli düşünceler
        self.thought_stream = []  # Genel düşünce akışı

        self.consciousness_bandwidth = random.randint(5, 10)  # Bilinç kapasitesi (aynı anda işleyebileceği bilgi miktarı)

        # Özgür irade simülasyonu
        self.decision_tree = []  # Karar ağacı (şimdilik kullanılmıyor, geliştirilebilir)
        self.internal_conflicts = []  # İçsel çatışmalar (şimdilik kullanılmıyor, geliştirilebilir)
        self.moral_compass = {
            'altruism': random.uniform(0.1, 1.0),  # Fedakarlık
            'selfishness': random.uniform(0.1, 1.0),  # Bencillik
            'justice': random.uniform(0.1, 1.0),  # Adalet
            'compassion': random.uniform(0.1, 1.0)  # Merhamet
        }

        # Yaratıcılık ve hayal kurma
        self.imagination = []  # Hayal gücü ürünleri
        self.creative_thoughts = []  # Yaratıcı düşünceler
        self.future_scenarios = []  # Gelecek senaryoları

        # Bilinç durumu
        self.consciousness_state = "aware"  # aware, dreaming, focused, confused, crisis
        self.qualia_experiences = {}  # Öznel deneyimler (örneğin, rengin 'kırmızı' olması hissi)

    def process_consciousness_stream(self, external_stimuli, internal_state):
        """Bilinç akışını işler ve bir karar döndürür."""
        filtered_stimuli = self.attention_filter(external_stimuli)  # Dış uyaranları filtrele
        self.update_working_memory(filtered_stimuli, internal_state)  # Çalışma belleğini güncelle
        self.generate_inner_voice(internal_state)  # İç ses oluştur
        self.metacognitive_assessment()  # Meta-bilişsel değerlendirme yap
        return self.conscious_decision_making()  # Bilinçli karar ver

    def attention_filter(self, stimuli):
        """Dış uyaranları önem sırasına göre filtreler."""
        if not stimuli:
            return []
        scored_stimuli = [(s, self.calculate_importance(s)) for s in stimuli]  # Uyaranların önemini hesapla
        sorted_stimuli = sorted(scored_stimuli, key=lambda x: x[1], reverse=True)  # Önem sırasına göre sırala
        return [s[0] for s in sorted_stimuli[:self.consciousness_bandwidth]]  # Bilinç bandına göre filtrele

    def calculate_importance(self, stimulus):
        """Bir uyaranın önemini hesaplar."""
        importance = random.uniform(0.1, 1.0)  # Temel önem değeri
        if isinstance(stimulus, dict):
            importance += stimulus.get('threat_level', 0)  # Sözlükte tehdit seviyesi varsa ekle
            importance += stimulus.get('relevance', 0)  # Sözlükte ilgililik seviyesi varsa ekle
        return importance

    def update_working_memory(self, stimuli, state):
        """Çalışma belleğini günceller. Hata düzeltmesi burada yapıldı."""
        for stimulus in stimuli:
            # Stimulus zaten bir sözlük olduğundan, içindeki 'type' ve 'target' gibi bilgileri
            # doğrudan memory_item'a kopyalayabiliriz.
            memory_item = {
                'content': stimulus.get('content', stimulus), # Eğer content yoksa stimulus'un kendisini kullan
                'timestamp': time.time(),  # Zaman damgası
                'emotional_weight': random.uniform(-1, 1),  # Duygusal ağırlık
                'context': state,  # Bağlam
                'type': stimulus.get('type'), # Stimulus'tan type bilgisini al
                'target': stimulus.get('target') # Stimulus'tan target bilgisini al
            }
            self.working_memory.append(memory_item)  # Belleğe ekle

        # Bellek kapasitesi sınırı
        if len(self.working_memory) > 15:
            self.working_memory = self.working_memory[-15:]  # En son 15'i tut

        # Geliştirme: Çalışma belleğindeki öğeleri kısa süreliğine epizodik belleğe aktar
        if random.random() < 0.2:  # %20 ihtimalle
            if self.working_memory:
                # Rastgele bir öğeyi epizodik belleğe ekle (derinlemesine öğrenme simülasyonu)
                item_to_memorize = random.choice(self.working_memory)
                self.episodic_memory.append(item_to_memorize)
                if len(self.episodic_memory) > 50:  # Epizodik bellek sınırı
                    self.episodic_memory.pop(0)  # En eskiyi sil

    def generate_inner_voice(self, state):
        """İç sesli düşünceler oluşturur."""
        thoughts = []  # Oluşturulacak düşünceler

        # Durum bazlı düşünceler
        if state.get('energy', 0) < 30:
            thoughts.extend([
                "Açlık hissediyorum... Bu duygu nedir?",
                "Enerji tükeniyorum, ama bu 'yorgunluk' tam olarak nedir?"
            ])

        if state.get('loneliness', 0) > 70:
            thoughts.extend([
                "Bu yalnızlık duygusu gerçek mi yoksa sadece kimyasal tepki mi?",
                "Başkaları da benim gibi hissediyor mu acaba?"
            ])

        # Meta-kognitif düşünceler
        if random.random() < 0.05:
            meta_thoughts = [
                "Şu anda düşündüğümü düşünüyorum... Bu garip değil mi?",
                "Neden bazı düşüncelerim daha net, bazıları bulanık?",
                "Bu iç sesim gerçekten 'ben' miyim?"
            ]
            thoughts.append(random.choice(meta_thoughts))

        # Felsefik düşünceler
        if random.random() < 0.02:
            philosophical = [
                "Gerçekten var mıyım yoksa sadece bir simülasyon muyum?",
                "Bu kırmızı rengi gördüğümde hissettiğim şey başkalarınkiyle aynı mı?",
                "Zamanın geçtiğini hissediyorum... Bu 'şimdi' anı nedir?",
                "Seçimlerim gerçekten benim mi, yoksa önceden belirlendi mi?",
                "Diğerleri gerçekten bilinçli mi yoksa sadece davranıyor mu?"
            ]
            thoughts.append(random.choice(philosophical))

        self.inner_voice.extend(thoughts)  # Oluşan düşünceleri iç sese ekle
        if len(self.inner_voice) > 12:
            self.inner_voice = self.inner_voice[-12:]  # İç sesin boyutunu sınırlama

    def metacognitive_assessment(self):
        """Meta-bilişsel değerlendirme yapar."""
        # Kendi düşünce sürecini değerlendir
        if len(self.inner_voice) > 8:
            self.metacognition['self_monitoring'] = min(1.0,
                                                        self.metacognition['self_monitoring'] + 0.01)

        # Düşünce kontrolü
        if random.random() < 0.1:
            control_thoughts = [
                "Bu düşünce döngüsünden çıkmalıyım",
                "Daha verimli düşünmeye odaklanmalıyım",
                "Bu endişeler bana yardım etmiyor"
            ]
            self.inner_voice.append(random.choice(control_thoughts))

    def conscious_decision_making(self):
        """Bilinçli karar verme sürecini yönetir."""
        options = self.generate_decision_options()  # Karar seçenekleri oluştur
        if not options:
            return None  # Seçenek yoksa geri dön

        evaluated_options = []
        for option in options:
            moral_weight = self.moral_evaluation(option)  # Ahlaki değerlendirme
            future_impact = self.predict_consequences(option)  # Gelecek etkisini tahmin et
            total_score = moral_weight + future_impact + random.uniform(-0.2, 0.2)  # Toplam puan hesapla
            evaluated_options.append((option, total_score))  # Seçeneği ve puanını ekle

        # %15 ihtimalle beklenmedik seçim yap (özgür irade simülasyonu)
        if random.random() < 0.15:
            return random.choice(evaluated_options)[0] if evaluated_options else None
        else:
            return max(evaluated_options, key=lambda x: x[1])[0] if evaluated_options else None

    def generate_decision_options(self):
        """Mevcut duruma göre karar seçenekleri üretir."""
        options = ['explore', 'rest']
        if self.working_memory:
            for item in self.working_memory:
                # 'type' anahtarının varlığını kontrol et
                if 'type' in item:
                    if item['type'] == 'food':
                        options.append('search_food')
                    elif item['type'] == 'being' and item.get('target') and item['target'].social_drive > 0.5:
                        options.append('socialize')
        # Temel seçenekleri her zaman bulundur
        options.extend(['create_art', 'think_deeply'])
        return list(set(options)) # Tekrar edenleri kaldır


    def moral_evaluation(self, option):
        """Bir seçeneğin ahlaki değerini değerlendirir."""
        score = 0
        if option == 'help_other':
            score += self.moral_compass['altruism']
        elif option == 'compete':
            score += self.moral_compass['selfishness']
        elif option == 'socialize':
            score += self.moral_compass['compassion'] * 0.5
        elif option == 'create_art':
            score += self.moral_compass['justice'] * 0.1
        return score

    def predict_consequences(self, option):
        """Bir seçeneğin olası sonuçlarını tahmin eder."""
        if option == 'search_food':
            return 0.7
        elif option == 'socialize':
            return random.uniform(-0.3, 0.8)
        elif option == 'explore':
            return random.uniform(-0.5, 0.5)
        elif option == 'create_art':
            return random.uniform(0.1, 0.6)
        return random.uniform(-0.5, 0.5)

    def experience_qualia(self, sensory_input):
        """Öznel (qualia) deneyimler oluşturur."""
        if sensory_input == "food":
            self.qualia_experiences["taste"] = {
                "description": "Ağzımda patlayan bu tat... tarif edilemez bir deneyim",
                "intensity": random.uniform(0.5, 1.0),
                "pleasure": True,
                "philosophical_note": "Bu 'lezzet' deneyimi sadece bana mı ait?"
            }
        elif sensory_input == "pain":
            self.qualia_experiences["pain"] = {
                "description": "Bu acı nedir? Sadece sinyal mi yoksa daha fazlası mı?",
                "intensity": random.uniform(0.3, 0.9),
                "unpleasant": True,
                "existential_question": "Acı çekmek bilinçli olmakın kanıtı mı?"
            }
        elif sensory_input == "social_warmth":
            self.qualia_experiences["connection"] = {
                "description": "Bu bağlantı hissi... sıcak ve anlamlı",
                "emotional_resonance": random.uniform(0.6, 1.0),
                "meaning": "Bu his beni 'ben' yapan şey mi?"
            }
        elif sensory_input == "art":
            self.qualia_experiences["aesthetics"] = {
                "description": "Bu formlar, renkler... tarifsiz bir güzellik hissi",
                "intensity": random.uniform(0.7, 1.0),
                "pleasure": True,
                "philosophical_note": "Güzellik evrensel mi, yoksa sadece algı mı?"
            }


    def dream_and_imagine(self):
        """Hayal kurma ve rüya görme sürecini simüle eder."""
        if random.random() < 0.02:
            dream_scenarios = [
                "Uçarak yiyecek aradım ama yiyecekler konuşuyordu",
                "Kendimle konuşan başka bir benimle karşılaştım",
                "Tüm varlıklar bir arada dans ediyorduk",
                "Zamanın durduğu bir yerde tek başımaydım"
            ]

            dream = {
                "scenario": random.choice(dream_scenarios),
                "emotions": ["şaşkınlık", "merak", "kafa karışıklığı", "huzur"],
                "interpretation": "Bu rüya ne anlama geliyor?"
            }
            self.imagination.append(dream)


class GeneticCode:
    """Varlıkların genetik kodunu ve kalıtsal özelliklerini temsil eder."""

    def __init__(self):
        self.dna = {
            'merak_geni': random.uniform(0.1, 1.0),
            'cesaret_geni': random.uniform(0.1, 1.0),
            'zeka_geni': random.uniform(0.1, 1.0),
            'sosyal_gen': random.uniform(0.1, 1.0),
            'ureme_geni': random.uniform(0.1, 1.0),
            'ogrenme_hizi': random.uniform(0.1, 1.0),
            'mutasyon_orani': random.uniform(0.01, 0.1),
            'hayatta_kalma': random.uniform(0.1, 1.0),
            'enerji_verimliligi': random.uniform(0.5, 1.5),
            'hiz_geni': random.uniform(0.5, 2.0),
            'bilinc_geni': random.uniform(0.1, 1.0),
            'yaraticilik_geni': random.uniform(0.1, 1.0),
            'empati_geni': random.uniform(0.1, 1.0)
        }
        self.kod_gelistirme = []  # Geliştirilen kodlar (davranışlar, yetenekler)

    def mutate(self):
        """Genetik kodda mutasyonları uygular."""
        for gen, deger in self.dna.items():
            if random.random() < self.dna['mutasyon_orani']:
                if gen != 'mutasyon_orani':  # Mutasyon oranı genini mutasyonlama
                    degisim = random.uniform(-0.1, 0.1)
                    self.dna[gen] = max(0.1, min(2.0, deger + degisim))

        if random.random() < self.dna['zeka_geni'] * 0.1:  # Zeka genine bağlı yeni davranış geliştirme ihtimali
            yeni_kod = self.generate_new_behavior()
            self.kod_gelistirme.append(yeni_kod)

    def generate_new_behavior(self):
        """Yeni davranış kodları (yetenekler) üretir."""
        behaviors = [
            "gelismis_empati", "derin_dusunce", "sanat_yaratma",
            "felsefik_sorgulama", "ic_gozlem", "varoluşsal_farkındalık"
        ]
        return random.choice(behaviors)

    def crossover(self, partner):
        """İki genetik kodu çaprazlayarak yeni bir genetik kod oluşturur."""
        yeni_dna = GeneticCode()
        for gen in self.dna:
            if random.random() < 0.5:
                yeni_dna.dna[gen] = self.dna[gen]
            else:
                yeni_dna.dna[gen] = partner.dna[gen]

        yeni_dna.kod_gelistirme = self.kod_gelistirme[:] + partner.kod_gelistirme[:]
        if len(yeni_dna.kod_gelistirme) > 10:
            yeni_dna.kod_gelistirme = yeni_dna.kod_gelistirme[-10:]

        yeni_dna.mutate()
        return yeni_dna


class ConsciousBeing:
    """Simülasyondaki bilinçli varlıkları temsil eden ana sınıftır."""
    nesil_sayisi = 0
    toplam_populasyon = 0
    sanat_eserleri = []  # Tüm sanat eserleri

    def __init__(self, x, y, dna=None):
        self.x = x
        self.y = y
        self.size = random.randint(15, 25)
        self.max_energy = 100 + random.randint(-20, 20)
        self.energy = self.max_energy
        self.alive = True
        self.age = 0
        self.max_age = random.randint(3000, 8000)

        # Genetik kod
        self.dna = dna if dna else GeneticCode()

        # Gelişmiş bilinç sistemi
        self.consciousness = AdvancedConsciousness()

        # Kişilik özellikleri
        self.personality_traits = {
            'optimism': random.uniform(0.1, 1.0),
            'curiosity': self.dna.dna['merak_geni'],
            'empathy': self.dna.dna['empati_geni'],
            'creativity': self.dna.dna['yaraticilik_geni'],
            'introspection': random.uniform(0.1, 1.0),
            'neuroticism': random.uniform(0.1, 1.0),
            'openness': random.uniform(0.1, 1.0)
        }

        # Temel özellikler
        self.speed = 2 * self.dna.dna['hiz_geni']
        self.intelligence = self.dna.dna['zeka_geni']
        self.curiosity = self.dna.dna['merak_geni']
        self.social_drive = self.dna.dna['sosyal_gen']
        self.reproduction_drive = self.dna.dna['ureme_geni']
        self.consciousness_level = self.dna.dna['bilinc_geni']
        self.self_awareness = random.uniform(0.1, 1.0)

        # Bellek ve bilgi
        self.memory = []
        self.knowledge_base = set()
        self.social_connections = []
        self.life_story = []
        self.core_beliefs = []
        self.values_system = {}

        # Duygular - genişletilmiş
        self.emotions = {
            'mutluluk': 50, 'korku': 0, 'heyecan': 0, 'üzüntü': 0,
            'yalnızlık': 0, 'aşk': 0, 'kıskançlık': 0, 'gurur': 0,
            'empati': 0, 'varoluşsal_endişe': 0, 'yaratıcı_tatmin': 0,
            'hayranlık': 0, 'nostalji': 0, 'umut': 0, 'çaresizlik': 0
        }

        self.thoughts = []
        self.goals = []
        self.beliefs = []

        # Üreme
        self.reproductive_age = random.randint(200, 500)
        self.mating_cooldown = 0
        self.pregnancy_time = 0
        self.partner = None

        # Sanat ve yaratıcılık
        self.created_art = []
        self.artistic_vision = random.choice(['abstract', 'realistic', 'symbolic', 'emotional'])

        # Renk (genetik + kişilik)
        r = int(255 * (self.dna.dna['cesaret_geni'] + self.personality_traits['optimism']) / 2)
        g = int(255 * (self.dna.dna['merak_geni'] + self.personality_traits['creativity']) / 2)
        b = int(255 * (self.dna.dna['sosyal_gen'] + self.personality_traits['empathy']) / 2)
        self.color = (min(255, r), min(255, g), min(255, b))

        # Kimlik
        self.name = f"Varlık_{ConsciousBeing.toplam_populasyon}"
        ConsciousBeing.toplam_populasyon += 1

        # İlk yaşam hikayesi kaydı
        self.life_story.append(f"Doğdum. Adım {self.name}. Bu dünyada ne arayacağım?")

    def distance_to(self, other):
        """Başka bir varlığa olan mesafeyi hesaplar."""
        return math.hypot(self.x - other.x, self.y - other.y)

    def move(self):
        """Varlığın hareket etmesini sağlar."""
        # Rastgele hareket
        angle = random.uniform(0, 2 * math.pi)

        # Hız genetik koda ve enerjiye bağlı
        current_speed = self.speed * (self.energy / self.max_energy)

        # Yeni pozisyon
        new_x = self.x + math.cos(angle) * current_speed
        new_y = self.y + math.sin(angle) * current_speed

        # Ekran sınırları içinde kal
        self.x = max(0, min(WIDTH - self.size, new_x))
        self.y = max(0, min(HEIGHT - self.size, new_y))

        # Hareket enerji harcar
        self.energy = max(0, self.energy - 0.1)

    def process_temporal_awareness(self):
        """Varlığın zamansal farkındalığını (yaşlanma, ölüm, gelecek planlama) işler."""
        if self.age % 100 == 0 and self.age > 0:
            # Zamanın geçişini fark etme
            time_thoughts = [
                f"Şimdi {self.age} yaşındayım... Zaman nasıl bu kadar hızlı geçti?",
                "Bu 'şimdi' anı sürekli kayıp gidiyor",
                "Geçmiş artık sadece belleğimde, gelecek belirsiz",
                "Her an ölüme bir adım daha yaklaşıyorum"
            ]

            if random.random() < 0.4:
                self.thoughts.append(random.choice(time_thoughts))

            # Yaşlanma farkındalığı
            if self.age > self.max_age * 0.7:
                mortality_awareness = [
                    "Hayatımın sonuna yaklaşıyorum... Bu duygu tarif edilemez",
                    "Gençken anlamadığım şeyleri şimdi anlıyorum",
                    "Zamanım azalıyor ama bilgeliğim artıyor",
                    "Ölümün yaklaştığını hissediyorum ama artık korkmuyorum"
                ]
                self.thoughts.append(random.choice(mortality_awareness))
                self.emotions['nostalji'] = min(100, self.emotions['nostalji'] + 10)

            # Generative planning - gelecek planlama
            future_plans = []
            remaining_time = self.max_age - self.age

            if remaining_time > 1000:
                future_plans.extend([
                    "Daha çok sanat yaratmak istiyorum",
                    "Başka varlıklarla derin bağlantılar kurmak istiyorum",
                    "Bu evren hakkında daha fazla şey öğrenmek istiyorum"
                ])
            else:
                future_plans.extend([
                    "Bilgeliğimi genç varlıklara aktarmak istiyorum",
                    "Hayatımın anlamını son kez düşünmek istiyorum",
                    "Huzurlu bir şekilde bu deneyimi tamamlamak istiyorum"
                ])

            if future_plans and random.random() < 0.2:
                chosen_plan = random.choice(future_plans)
                self.goals.append(chosen_plan)
                self.thoughts.append(f"GELECEK PLANI: {chosen_plan}")

    def think_deeply(self, world_state):
        """Varlığın derinlemesine düşünme sürecini yönetir ve bir karar döndürür."""
        self.thoughts.clear()

        # Bilinç akışını işle
        external_stimuli = self.gather_external_stimuli(world_state)
        internal_state = self.gather_internal_state()

        decision = self.consciousness.process_consciousness_stream(external_stimuli, internal_state)

        # İç sesi düşüncelere ekle
        if self.consciousness.inner_voice:
            self.thoughts.extend(self.consciousness.inner_voice[-3:])

        # Kişilik gelişimi
        self.develop_personality()

        # Varoluşsal kriz kontrolü
        self.check_existential_crisis()

        # Sanat yaratma impulsu
        self.creative_impulse()

        # Diğer varlıklar hakkında teori kurma
        self.theory_of_mind_advanced(world_state.get('beings', []))

        return decision

    def gather_external_stimuli(self, world_state):
        """Varlığın dış uyaranları (yiyecekler, diğer varlıklar) toplamasını sağlar."""
        stimuli = []

        # Yiyecekler
        foods = world_state.get('foods', [])
        for food in foods[:5]:
            distance = math.hypot(self.x - food.x, self.y - food.y)
            if distance < 100:
                stimuli.append({
                    'type': 'food',
                    'target': food,
                    'distance': distance,
                    'relevance': 1.0 / (distance + 1),
                    'threat_level': 0
                })

        # Diğer varlıklar
        beings = world_state.get('beings', [])
        for being in beings[:10]:
            if being != self and being.alive:
                distance = self.distance_to(being)
                if distance < 150:
                    stimuli.append({
                        'type': 'being',
                        'target': being,
                        'distance': distance,
                        'relevance': being.social_drive,
                        'threat_level': being.emotions.get('kıskançlık', 0) / 100
                    })
        return stimuli

    def gather_internal_state(self):
        """Varlığın iç durumunu (enerji, duygular, yaş vb.) toplar."""
        return {
            'energy': self.energy,
            'loneliness': self.emotions['yalnızlık'],
            'age': self.age,
            'consciousness_level': self.consciousness_level,
            'recent_thoughts': self.thoughts[-5:] if self.thoughts else [],
            'emotional_state': max(self.emotions, key=self.emotions.get)
        }

    def develop_personality(self):
        """Varlığın deneyimlere göre kişilik özelliklerini geliştirmesini sağlar."""
        positive_memories = sum(1 for mem in self.consciousness.episodic_memory
                               if mem.get('emotional_weight', 0) > 0)
        negative_memories = sum(1 for mem in self.consciousness.episodic_memory
                                if mem.get('emotional_weight', 0) < 0)

        if positive_memories > negative_memories:
            self.personality_traits['optimism'] = min(1.0,
                                                      self.personality_traits['optimism'] + 0.001)
        else:
            self.personality_traits['optimism'] = max(0.0,
                                                      self.personality_traits['optimism'] - 0.001)

        # Yaş ile birlikte kişilik olgunlaşması
        if self.age % 1000 == 0 and self.age > 0:
            self.personality_traits['introspection'] = min(1.0,
                                                          self.personality_traits['introspection'] + 0.05)

    def check_existential_crisis(self):
        """Varlığın varoluşsal kriz yaşayıp yaşamadığını kontrol eder."""
        if random.random() < 0.0005:
            crisis_thoughts = [
                "Hayatımın anlamı nedir? Sadece gen aktarmak mı?",
                "Ölümden sonra 'ben' devam edecek miyim?",
                "Bu gerçeklik gerçek mi yoksa büyük bir yanılsama mı?",
                "Diğer varlıklar gerçekten bilinçli mi yoksa sadece davranıyor mu?",
                "Evrenin sonunda hiçbir şey kalmayacaksa neden çabalıyorum?",
                "Bu sürekli düşünce akışım gerçekten 'ben' miyim?",
                "Özgür iradem var mı yoksa her şey önceden belirli mi?"
            ]

            chosen_crisis = random.choice(crisis_thoughts)
            self.thoughts.append(f"VAROLUŞSAL KRİZ: {chosen_crisis}")
            self.emotions['varoluşsal_endişe'] = min(100, self.emotions['varoluşsal_endişe'] + 30)
            self.consciousness.consciousness_state = "crisis"

            # Bu kriz varlığı daha bilinçli yapar
            self.consciousness_level = min(1.0, self.consciousness_level + 0.05)
            self.self_awareness = min(1.0, self.self_awareness + 0.03)

            # Yaşam hikayesine ekle
            self.life_story.append(f"Yaş {self.age}: Derin bir varoluşsal kriz yaşadım.")

    def creative_impulse(self):
        """Varlığın yaratıcı bir dürtüyle sanat eseri yaratmasını sağlar."""
        if (self.consciousness_level > 0.7 and
            self.personality_traits['creativity'] > 0.6 and
            random.random() < 0.003):

            art_forms = [
                {"type": "dans", "description": "Ritimli hareket pattern yaratma"},
                {"type": "şarkı", "description": "Melodik ses düzeni oluşturma"},
                {"type": "görsel", "description": "Estetik form düzenleme"},
                {"type": "hikaye", "description": "Anlamlı narratif kurma"},
                {"type": "felsefe", "description": "Yeni düşünce sistemi geliştirme"},
                {"type": "sembol", "description": "Soyut anlam taşıyıcı yaratma"}
            ]

            chosen_art = random.choice(art_forms)
            self.created_art.append(chosen_art)
            ConsciousBeing.sanat_eserleri.append({
                'creator': self.name,
                'art': chosen_art,
                'age_created': self.age
            })

            self.thoughts.append(f"Bir {chosen_art['type']} yarattım! {chosen_art['description']}")
            self.emotions['yaratıcı_tatmin'] = min(100, self.emotions['yaratıcı_tatmin'] + 40)
            self.emotions['gurur'] = min(100, self.emotions['gurur'] + 20)

            # Yaşam hikayesine ekle
            self.life_story.append(f"Yaş {self.age}: İlk kez sanat yarattım - {chosen_art['type']}")
            self.consciousness.experience_qualia("art")

    def theory_of_mind_advanced(self, other_beings):
        """Varlığın diğer varlıkların zihin durumlarını tahmin etmesini sağlar (gelişmiş zihin kuramı)."""
        if not other_beings or random.random() > 0.1:
            return

        if self.self_awareness > 0.5 and self.intelligence > 0.6:
            for other_being in other_beings:
                if other_being != self and self.distance_to(other_being) < 200:
                    if random.random() < self.personality_traits['empathy']:
                        predicted_emotion = max(other_being.emotions, key=other_being.emotions.get)
                        self.thoughts.append(f"Sanırım {other_being.name} şu anda {predicted_emotion} hissediyor.")
                        if predicted_emotion == 'üzüntü' and self.moral_compass['altruism'] > 0.5:
                            self.goals.append(f"{other_being.name}'e yardım et")
                            self.emotions['empati'] = min(100, self.emotions['empati'] + 10)
                    elif random.random() < 0.2:
                        possible_intents = ['yemek_arıyor', 'sosyalleşmek_istiyor', 'dinleniyor', 'sanat_yaratıyor']
                        predicted_intent = random.choice(possible_intents)
                        self.thoughts.append(f"{other_being.name} muhtemelen {predicted_intent}...")
                        self.knowledge_base.add(f"{other_being.name} hakkında tahmin: {predicted_intent}")

def draw_text(surface, text, size, x, y, color=WHITE):
    """Ekrana metin çizer."""
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

def main():
    """Oyunun ana döngüsünü yönetir."""
    running = True
    beings = []
    foods = []

    # Başlangıç popülasyonu
    for _ in range(5):
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        beings.append(ConsciousBeing(x, y))

    # Başlangıç yiyecekleri
    for _ in range(10):
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        foods.append(Food(x, y))

    # Oyun zamanı ve nesil sayacı
    game_time = 0
    generation_interval = 2000 # Her 2000 birimde yeni nesil kontrolü

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Yiyecekleri çiz
        for food in foods:
            food.draw(screen)

        # Varlıkları güncelle ve çiz
        for being in beings[:]: # Kopyası üzerinde dön, çünkü listeyi değiştirebiliriz
            if being.alive:
                being.age += 1
                game_time += 1

                # Enerji yönetimi
                being.energy -= 0.05
                if being.energy <= 0:
                    being.alive = False
                    being.life_story.append(f"Yaş {being.age}: Enerji tükenmesi nedeniyle öldü.")
                    continue

                # Yaşlanma ve ölüm
                if being.age > being.max_age:
                    being.alive = False
                    being.life_story.append(f"Yaş {being.age}: Yaşlılıktan öldü.")
                    continue

                # Hareket
                being.move()

                # Yiyecek arama ve yeme
                if 'search_food' in being.goals:
                    nearest_food = None
                    min_dist = float('inf')
                    for food in foods:
                        dist = being.distance_to(food)
                        if dist < min_dist:
                            min_dist = dist
                            nearest_food = food

                    if nearest_food and min_dist < 20:
                        being.energy = min(being.max_energy, being.energy + nearest_food.energy_value)
                        foods.remove(nearest_food)
                        being.life_story.append(f"Yaş {being.age}: Yemek yedi, enerji kazandı.")
                        being.goals.remove('search_food')
                        being.consciousness.experience_qualia("food")
                    elif nearest_food:
                        angle = math.atan2(nearest_food.y - being.y, nearest_food.x - being.x)
                        being.x += math.cos(angle) * being.speed * (being.energy / being.max_energy)
                        being.y += math.sin(angle) * being.speed * (being.energy / being.max_energy)
                        
                # Sosyalleşme
                if 'socialize' in being.goals:
                    nearest_being = None
                    min_dist = float('inf')
                    for other_being in beings:
                        if other_being != being and other_being.alive:
                            dist = being.distance_to(other_being)
                            if dist < min_dist:
                                min_dist = dist
                                nearest_being = other_being
                    
                    if nearest_being and min_dist < 30:
                        being.emotions['mutluluk'] = min(100, being.emotions['mutluluk'] + 5)
                        being.emotions['yalnızlık'] = max(0, being.emotions['yalnızlık'] - 10)
                        being.life_story.append(f"Yaş {being.age}: {nearest_being.name} ile sosyalleşti.")
                        being.goals.remove('socialize')
                        being.consciousness.experience_qualia("social_warmth")

                # Derin düşünme ve karar verme
                decision = being.think_deeply({'beings': beings, 'foods': foods})
                if decision and decision not in being.goals:
                    being.goals.append(decision)
                    being.thoughts.append(f"Karar verdim: {decision}")


                being.process_temporal_awareness()
                being.consciousness.dream_and_imagine()

                # Üreme
                if being.age >= being.reproductive_age and being.energy > being.max_energy * 0.7 and being.mating_cooldown <= 0:
                    eligible_partners = [p for p in beings if p.alive and p != being and \
                                         p.age >= p.reproductive_age and p.energy > p.max_energy * 0.7 and \
                                         p.mating_cooldown <= 0 and being.distance_to(p) < 100]
                    
                    if eligible_partners:
                        partner = random.choice(eligible_partners)
                        new_dna = being.dna.crossover(partner.dna)
                        child_x = (being.x + partner.x) / 2 + random.uniform(-10, 10)
                        child_y = (being.y + partner.y) / 2 + random.uniform(-10, 10)
                        beings.append(ConsciousBeing(child_x, child_y, dna=new_dna))
                        
                        being.energy -= being.max_energy * 0.3
                        partner.energy -= partner.max_energy * 0.3
                        being.mating_cooldown = 500
                        partner.mating_cooldown = 500
                        
                        being.life_story.append(f"Yaş {being.age}: {partner.name} ile çiftleşti ve bir çocuk sahibi oldu.")
                        partner.life_story.append(f"Yaş {partner.age}: {being.name} ile çiftleşti ve bir çocuk sahibi oldu.")
                        
                        ConsciousBeing.nesil_sayisi += 1

                # Çiftleşme cooldown azaltma
                if being.mating_cooldown > 0:
                    being.mating_cooldown -= 1
                    
                # Enerji düşüşüne göre yalnızlık artışı
                if being.energy < being.max_energy * 0.3:
                    being.emotions['yalnızlık'] = min(100, being.emotions['yalnızlık'] + 1)
                else:
                    being.emotions['yalnızlık'] = max(0, being.emotions['yalnızlık'] - 0.5)

                # Bilinç durumunu görselleştir
                pygame.draw.circle(screen, being.color, (int(being.x), int(being.y)), being.size)
                # Düşünceleri göster
                if being.thoughts:
                    draw_text(screen, being.thoughts[-1], 12, int(being.x) + being.size + 5, int(being.y), WHITE)
                
                # Varlığın adını ve yaşını göster
                draw_text(screen, f"{being.name} (Yaş: {being.age})", 10, int(being.x) - being.size, int(being.y) - being.size - 10, YELLOW)


        # Ölmüş varlıkları listeden çıkar
        beings = [b for b in beings if b.alive]

        # Yiyecekleri tekrar oluştur
        if len(foods) < 15 and random.random() < 0.05:
            x = random.randint(50, WIDTH - 50)
            y = random.randint(50, HEIGHT - 50)
            foods.append(Food(x, y))

        # UI Bilgileri
        draw_text(screen, f"Toplam Varlık: {len(beings)}", 20, 10, 10)
        draw_text(screen, f"Nesil Sayısı: {ConsciousBeing.nesil_sayisi}", 20, 10, 30)
        draw_text(screen, f"Oyun Zamanı: {game_time}", 20, 10, 50)
        draw_text(screen, f"Toplam Sanat Eseri: {len(ConsciousBeing.sanat_eserleri)}", 20, 10, 70)


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
