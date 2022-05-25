# Generated by Django 4.0.4 on 2022-05-18 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0030_denemeadres'),
    ]

    operations = [
        migrations.AddField(
            model_name='denemeadres',
            name='district',
            field=models.CharField(choices=[('AHM', 'AHMET REMZİ YÜREĞİR MAHALLESİ'), ('AKK', 'AKKAPI MAHALLESİ'), ('ALİ', 'ALİDEDE MAHALLESİ'), ('AYD', 'AYDINLAR MAHALLESİ'), ('BAH', 'BAHÇELİEVLER MAHALLESİ'), ('BAR', 'BARBAROS MAHALLESİ'), ('BAR', 'BARIŞ MAHALLESİ'), ('BEL', 'BELEDİYE EVLERİ MAHALLESİ'), ('BEŞ', 'BEŞOCAK MAHALLESİ'), ('BEY', 'BEY MAHALLESİ'), ('BEY', 'BEYAZEVLER MAHALLESİ'), ('CEM', 'CEMALPAŞA MAHALLESİ'), ('ÇIN', 'ÇINARLI MAHALLESİ'), ('DAĞ', 'DAĞLIOĞLU MAHALLESİ'), ('DEM', 'DEMETEVLER MAHALLESİ'), ('DEN', 'DENİZLİ MAHALLESİ'), ('DÖŞ', 'DÖŞEME MAHALLESİ'), ('DUM', 'DUMLUPINAR MAHALLESİ'), ('EME', 'EMEK MAHALLESİ'), ('FAT', 'FATİH MAHALLESİ'), ('FEV', 'FEVZİPAŞA MAHALLESİ'), ('GAZ', 'GAZİPAŞA MAHALLESİ'), ('GÜL', 'GÜLBAHÇESİ MAHALLESİ'), ('GÜL', 'GÜLPINAR MAHALLESİ'), ('GÜR', 'GÜRSELPAŞA MAHALLESİ'), ('GÜZ', 'GÜZELYALI MAHALLESİ'), ('HAN', 'HANEDAN MAHALLESİ'), ('HAV', 'HAVUZLUBAHÇE MAHALLESİ'), ('HUR', 'HURMALI MAHALLESİ'), ('HUZ', 'HUZUREVLERİ MAHALLESİ'), ('HÜR', 'HÜRRİYET MAHALLESİ'), ('İSM', 'İSMETPAŞA MAHALLESİ'), ('İST', 'İSTİKLAL MAHALLESİ'), ('KAR', 'KARASOKU MAHALLESİ'), ('KAY', 'KAYALIBAĞ MAHALLESİ'), ('KOC', 'KOCAVEZİR MAHALLESİ'), ('KUR', 'KURTULUŞ MAHALLESİ'), ('KUR', 'KURUKÖPRÜ MAHALLESİ'), ('MAH', 'MAHFESIĞMAZ MAHALLESİ'), ('MES', 'MESTANZADE MAHALLESİ'), ('MEY', 'MEYDAN MAHALLESİ'), ('MID', 'MIDIK MAHALLESİ'), ('MİR', 'MİRZAÇELEBİ MAHALLESİ'), ('MİT', 'MİTHATPAŞA MAHALLESİ'), ('NAM', 'NAMIK KEMAL MAHALLESİ'), ('NAR', 'NARLICA MAHALLESİ'), ('ONU', 'ONUR MAHALLESİ'), ('OVA', 'OVA MAHALLESİ'), ('PIN', 'PINAR MAHALLESİ'), ('REŞ', 'REŞATBEY MAHALLESİ'), ('SAK', 'SAKARYA MAHALLESİ'), ('SAR', 'SARIYAKUP MAHALLESİ'), ('SUC', 'SUCUZADE MAHALLESİ'), ('SÜM', 'SÜMER MAHALLESİ'), ('ŞAK', 'ŞAKİRPAŞA MAHALLESİ'), ('ŞEH', 'ŞEHİTDURAN MAHALLESİ'), ('TEP', 'TEPEBAĞ MAHALLESİ'), ('TOR', 'TOROS MAHALLESİ'), ('TÜR', 'TÜRKOCAĞI MAHALLESİ'), ('UÇA', 'UÇAK MAHALLESİ'), ('ULU', 'ULUCAMİİ MAHALLESİ'), ('YEN', 'YENİBARAJ MAHALLESİ'), ('YEN', 'YENİBEY MAHALLESİ'), ('TEL', 'TELLİDERE MAHALLESİ'), ('YEŞ', 'YEŞİLEVLER MAHALLESİ'), ('YEŞ', 'YEŞİLOBA MAHALLESİ'), ('YEŞ', 'YEŞİLYURT MAHALLESİ'), ('YEŞ', 'YEŞİLYUVA MAHALLESİ'), ('YUR', 'YURT MAHALLESİ'), ('YÜZ', 'YÜZÜNCÜYIL MAHALLESİ'), ('ZİY', 'ZİYAPAŞA MAHALLESİ'), ('200', '2000 EVLER MAHALLESİ'), ('BÜY', 'BÜYÜKÇILDIRIM MAHALLESİ'), ('BÜY', 'BÜYÜKDİKİLİ MAHALLESİ'), ('CAM', 'CAMUZCU MAHALLESİ'), ('GÖK', 'GÖKÇELER MAHALLESİ'), ('GÖL', 'GÖLBAŞI MAHALLESİ'), ('KAR', 'KARAKUYU MAHALLESİ'), ('KAR', 'KARSLILAR MAHALLESİ'), ('KOY', 'KOYUNCU MAHALLESİ'), ('KUR', 'KURTTEPE MAHALLESİ'), ('KUY', 'KUYUMCULAR MAHALLESİ'), ('KÜÇ', 'KÜÇÜKÇILDIRIM MAHALLESİ'), ('SAR', 'SARIHAMZALI MAHALLESİ'), ('SAR', 'SARIHUĞLAR MAHALLESİ'), ('ŞAM', 'ŞAMBAYADI MAHALLESİ'), ('YAL', 'YALMANLI MAHALLESİ'), ('YEN', 'YENİDAM MAHALLESİ'), ('YOL', 'YOLGEÇEN MAHALLESİ'), ('ZEY', 'ZEYTİNLİ MAHALLESİ'), ('BAH', 'BAHÇEŞEHİR MAHALLESİ'), ('YEN', 'YENİ  MAHALLESİ'), ('ESE', 'ESENTEPE MAHALLESİ'), ('HAD', 'HADIRLI MAHALLESİ'), ('KAR', 'KARAYUSUFLU MAHALLESİ'), ('SER', 'SERİNEVLER MAHALLESİ'), ('KAY', 'KAYIŞLI MAHALLESİ'), ('SAL', 'SALMANBEYLİ MAHALLESİ'), ('DER', 'DERVİŞLER MAHALLESİ'), ('ÇAP', 'ÇAPUTÇU MAHALLESİ'), ('KÖY', 'KÖYLÜOĞLU MAHALLESİ'), ('DÖR', 'DÖRTAĞAÇ MAHALLESİ'), ('MÜR', 'MÜRSELOĞLU MAHALLESİ'), ('KOZ', 'KOZA MAHALLESİ'), ('KÜÇ', 'KÜÇÜKDİKİLİ MAHALLESİ'), ('KAV', 'KAVAKLI MAHALLESİ'), ('MEK', 'MEKAN MAHALLESİ'), ('SÖĞ', 'SÖĞÜTLÜ MAHALLESİ'), ('AKD', 'AKDENİZ MAHALLESİ'), ('AKI', 'AKINCILAR MAHALLESİ'), ('ANA', 'ANADOLU MAHALLESİ'), ('BAH', 'BAHÇELİEVLER MAHALLESİ'), ('BAŞ', 'BAŞAK MAHALLESİ'), ('ÇAM', 'ÇAMLIBEL MAHALLESİ'), ('DER', 'DERVİŞLER MAHALLESİ'), ('GÜN', 'GÜNEŞLİ MAHALLESİ'), ('HAY', 'HAYDAROĞLU MAHALLESİ'), ('KAR', 'KARACAOĞLAN MAHALLESİ'), ('KAZ', 'KAZIM KARABEKİR MAHALLESİ'), ('KIŞ', 'KIŞLA MAHALLESİ'), ('KİR', 'KİREMİTHANE MAHALLESİ'), ('KÖP', 'KÖPRÜLÜ MAHALLESİ'), ('LEV', 'LEVENT MAHALLESİ'), ('ÖZG', 'ÖZGÜR MAHALLESİ'), ('P.T', 'P.T.T MAHALLESİ'), ('REM', 'REMZİ OĞUZ ARIK MAHALLESİ'), ('SEL', 'SELAHATTİN EYYUBİ MAHALLESİ'), ('SER', 'SERİNEVLER MAHALLESİ'), ('SEY', 'SEYHAN MAHALLESİ'), ('SİN', 'SİNANPAŞA MAHALLESİ'), ('ŞEH', 'ŞEHİT ERKUT AKBAY MAHALLESİ'), ('TAH', 'TAHSİLLİ MAHALLESİ'), ('ULU', 'ULUBATLI HASAN MAHALLESİ'), ('YAM', 'YAMAÇLI MAHALLESİ'), ('YAV', 'YAVUZLAR MAHALLESİ'), ('19 ', '19 MAYIS MAHALLESİ'), ('ÇIN', 'ÇINARLI MAHALLESİ'), ('MUT', 'MUTLU MAHALLESİ'), ('DED', 'DEDE KORKUT MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('YUN', 'YUNUS EMRE MAHALLESİ'), ('YEŞ', 'YEŞİL BAĞLAR MAHALLESİ'), ('KOZ', 'KOZA MAHALLESİ'), ('GÜZ', 'GÜZELEVLER MAHALLESİ'), ('YEN', 'YENİDOĞAN MAHALLESİ'), ('ATA', 'ATAKENT MAHALLESİ'), ('SAR', 'SARIÇAM MAHALLESİ'), ('DAD', 'DADALOĞLU MAHALLESİ'), ('MEH', 'MEHMET AKİF ERSOY MAHALLESİ'), ('YIL', 'YILDIRIM BEYAZIT MAHALLESİ'), ('BAY', 'BAYRAM HACILI MAHALLESİ'), ('AYV', 'AYVALI MAHALLESİ'), ('İST', 'İSTİKLAL MAHALLESİ'), ('BUR', 'BURUK CUMHURİYET MAHALLESİ'), ('İNC', 'İNCİRLİK CUMHURİYET MAHALLESİ'), ('HÜR', 'HÜRRİYET MAHALLESİ'), ('KEM', 'KEMALPAŞA MAHALLESİ'), ('YEN', 'YENİ MAHALLESİ'), ('ESE', 'ESENTEPE MAHALLESİ'), ('ORH', 'ORHANGAZİ MAHALLESİ'), ('SOF', 'SOFUDEDE MAHALLESİ'), ('ŞAH', 'ŞAHİNTEPE MAHALLESİ'), ('YEŞ', 'YEŞİLTEPE MAHALLESİ'), ('YAV', 'YAVUZ SULTAN SELİM MAHALLESİ'), ('BEY', 'BEYCELİ MAHALLESİ'), ('GÜL', 'GÜLTEPE MAHALLESİ'), ('DOĞ', 'DOĞANKENT BAHÇELİEVLER MAHALLESİ'), ('DOĞ', 'DOĞANKENT CUMHURİYET MAHALLESİ'), ('GAZ', 'GAZİPAŞA MAHALLESİ'), ('DOĞ', 'DOĞANKENT KIŞLA MAHALLESİ'), ('PEK', 'PEKMEZLİ MAHALLESİ'), ('AĞZ', 'AĞZIBÜYÜK MAHALLESİ'), ('DAN', 'DANIŞMENT MAHALLESİ'), ('DEN', 'DENİZKUYUSU MAHALLESİ'), ('SAĞ', 'SAĞDIÇLI MAHALLESİ'), ('ŞEY', 'ŞEYHMURAT MAHALLESİ'), ('TAŞ', 'TAŞÇI MAHALLESİ'), ('HAV', 'HAVUTLU MAHALLESİ'), ('AYD', 'AYDINCIK MAHALLESİ'), ('KAY', 'KAYARLI MAHALLESİ'), ('YUK', 'YUKARIÇİÇEKLİ MAHALLESİ'), ('ALİ', 'ALİHOCALI  MAHALLESİ'), ('KÖK', 'KÖKLÜCE MAHALLESİ'), ('ATA', 'ATATÜRK MAHALLESİ'), ('SOL', 'SOLAKLI CUMHURİYET MAHALLESİ'), ('SOL', 'SOLAKLI HÜRRİYET MAHALLESİ'), ('SAZ', 'SAZAK MAHALLESİ'), ('ŞAH', 'ŞAHİNAĞA MAHALLESİ'), ('PAŞ', 'PAŞAKÖY MAHALLESİ'), ('YAL', 'YALNIZCA MAHALLESİ'), ('AKD', 'AKDAM MAHALLESİ'), ('EĞR', 'EĞRİAĞAÇ MAHALLESİ'), ('ZAĞ', 'ZAĞARLI MAHALLESİ'), ('KAM', 'KAMIŞLI MAHALLESİ'), ('GÖK', 'GÖKÇELİ MAHALLESİ'), ('YEN', 'YENİCE MAHALLESİ'), ('BEY', 'BEYKÖY MAHALLESİ'), ('ÇAĞ', 'ÇAĞIRKANLI MAHALLESİ'), ('KÖP', 'KÖPRÜGÖZÜ MAHALLESİ'), ('YUN', 'YUNUSOĞLU CUMHURİYET MAHALLESİ'), ('YUN', 'YUNUSOĞLU HÜRRİYET MAHALLESİ'), ('SAK', 'SAKIZLI MAHALLESİ'), ('HAC', 'HACIALİ MAHALLESİ'), ('CİN', 'CİNE MAHALLESİ'), ('YEN', 'YENİKÖY MAHALLESİ'), ('GÜM', 'GÜMÜŞYAZI MAHALLESİ'), ('KAD', 'KADIKÖY MAHALLESİ'), ('YER', 'YERDELEN MAHALLESİ'), ('IRM', 'IRMAKBAŞI MAHALLESİ'), ('CIR', 'CIRIK MAHALLESİ'), ('KAR', 'KARAAHMETLİ MAHALLESİ'), ('ESK', 'ESKİ MİSİS MAHALLESİ'), ('YAK', 'YAKAPINAR MAHALLESİ'), ('ABD', 'ABDİOĞLU CUMHURİYET MAHALLESİ'), ('ÖZL', 'ÖZLER MAHALLESİ'), ('BÜY', 'BÜYÜKKAPILI MAHALLESİ'), ('HER', 'HEREKLİ MAHALLESİ'), ('ÇOT', 'ÇOTLU MAHALLESİ'), ('DÜZ', 'DÜZCE MAHALLESİ'), ('ESE', 'ESENLER MAHALLESİ'), ('KÜT', 'KÜTÜKLÜ MAHALLESİ'), ('YAH', 'YAHŞİLER MAHALLESİ'), ('KÜÇ', 'KÜÇÜKBAKLALI MAHALLESİ'), ('BÜY', 'BÜYÜK BAKLALI MAHALLESİ'), ('HAV', 'HAVRANİYE MAHALLESİ'), ('GEÇ', 'GEÇİTLİ CUMHURİYET MAHALLESİ'), ('GÖZ', 'GÖZTEPE MAHALLESİ'), ('MÜM', 'MÜMİNLİ MAHALLESİ'), ('YÜR', 'YÜREKLİ MAHALLESİ'), ('DAĞ', 'DAĞCI MAHALLESİ'), ('DED', 'DEDEPINARI MAHALLESİ'), ('CAM', 'CAMİLİ MAHALLESİ'), ('SUL', 'SULUCA MAHALLESİ'), ('ACI', 'ACIDERE MAHALLESİ'), ('ACI', 'ACIDEREOSB MAHALLESİ'), ('AKP', 'AKPINAR MAHALLESİ'), ('BAŞ', 'BAŞPINAR MAHALLESİ'), ('MAN', 'MANSURLU MAHALLESİ'), ('SİN', 'SİNANPAŞA MAHALLESİ'), ('ADA', 'ADATEPE MAHALLESİ'), ('AYD', 'AYDEMİROĞLU MAHALLESİ'), ('BEL', 'BELEDİYE EVLERİ MAHALLESİ'), ('BÜY', 'BÜYÜKKIRIM MAHALLESİ'), ('BOT', 'BOTA MAHALLESİ'), ('BUR', 'BURHANİYE MAHALLESİ'), ('CİV', 'CİVANTAYAK MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('EME', 'EMEK MAHALLESİ'), ('ESE', 'ESENTEPE MAHALLESİ'), ('FAT', 'FATİH SULTAN MEHMET MAHALLESİ'), ('GAZ', 'GAZİ OSMAN PAŞA MAHALLESİ'), ('ŞEH', 'ŞEHİT HACI İBRAHİM MAHALLESİ'), ('HÜR', 'HÜRRİYET MAHALLESİ'), ('İNÖ', 'İNÖNÜ MAHALLESİ'), ('İST', 'İSTİKLAL MAHALLESİ'), ('ZÜB', 'ZÜBEYDE HANIM MAHALLESİ'), ('KEL', 'KELEMETİ MAHALLESİ'), ('KÜÇ', 'KÜÇÜKKIRIM MAHALLESİ'), ('KON', 'KONAKOĞLU MAHALLESİ'), ('KOR', 'KORUKLU MAHALLESİ'), ('MİT', 'MİTHAT PAŞA MAHALLESİ'), ('MOD', 'MODERNEVLER MAHALLESİ'), ('MUR', 'MURADİYE MAHALLESİ'), ('NAM', 'NAMIK KEMAL MAHALLESİ'), ('SAR', 'SARISAKAL MAHALLESİ'), ('ŞAH', 'ŞAHİN ÖZBİLEN MAHALLESİ'), ('ATA', 'ATATÜRK MAHALLESİ'), ('ULU', 'ULUS MAHALLESİ'), ('YAR', 'YARSUAT MAHALLESİ'), ('ALT', 'ALTIOCAK MAHALLESİ'), ('BEL', 'BELENKÖY MAHALLESİ'), ('GÖK', 'GÖKÇELİ MAHALLESİ'), ('KAR', 'KARACAUŞAĞI MAHALLESİ'), ('KAZ', 'KAZANCI MAHALLESİ'), ('YEŞ', 'YEŞİL DÜŞMÜŞ MAHALLESİ'), ('SÜL', 'SÜLEMİŞLİ MAHALLESİ'), ('KEK', 'KEKLİKÇİ MAHALLESİ'), ('KAR', 'KARACAOĞLAN MAHALLESİ'), ('İSL', 'İSLAM MAHALLESİ'), ('ADA', 'ADALET MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('HÜR', 'HÜRRİYET MAHALLESİ'), ('MEN', 'MENTEŞ MAHALLESİ'), ('TUN', 'TUNA MAHALLESİ'), ('SAY', 'SAYGEÇİT MAHALLESİ'), ('KOC', 'KOCAVELİLER MAHALLESİ'), ('KAR', 'KARAPINAR   MAHALLESİ'), ('SEL', 'SELAMPINAR MAHALLESİ'), ('ÇEC', 'ÇECELİ MAHALLESİ'), ('AKT', 'AKTAŞ MAHALLESİ'), ('SAY', 'SAYPINAR MAHALLESİ'), ('GÜV', 'GÜVENÇ MAHALLESİ'), ('BAŞ', 'BAŞKIF MAHALLESİ'), ('KAP', 'KAPIKAYA MAHALLESİ'), ('SAL', 'SALBAŞ ESENTEPE MAHALLESİ'), ('KOC', 'KOCATEPE MAHALLESİ'), ('YEN', 'YENİ MAHALLESİ'), ('GÖK', 'GÖKKUYU MAHALLESİ'), ('ÇAT', 'ÇATALAN MAHALLESİ'), ('SAR', 'SARIMEHMETLİ MAHALLESİ'), ('KAR', 'KARŞIYAKA MAHALLESİ'), ('KEM', 'KEMALİYE MAHALLESİ'), ('ORT', 'ORTA MAHALLESİ'), ('YEN', 'YENİ MAHALLESİ'), ('ARS', 'ARSLANPAŞA MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('HAC', 'HACIUŞAĞI MAHALLESİ'), ('MAH', 'MAHMUTLU MAHALLESİ'), ('ŞEV', 'ŞEVKİYE MAHALLESİ'), ('TAŞ', 'TAŞ MAHALLESİ'), ('TUF', 'TUFANPAŞA MAHALLESİ'), ('YAR', 'YARIMOĞLU MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('İST', 'İSTİKLAL MAHALLESİ'), ('KUR', 'KURTULUŞ MAHALLESİ'), ('ZAF', 'ZAFER MAHALLESİ'), ('FAT', 'FATİH MAHALLESİ'), ('İSL', 'İSLAM MAHALLESİ'), ('YEŞ', 'YEŞİLBAĞLAR MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('İST', 'İSTİKLAL MAHALLESİ'), ('YEN', 'YENİCAMİ MAHALLESİ'), ('AKD', 'AKDENİZ MAHALLESİ'), ('AKY', 'AKYUVA MAHALLESİ'), ('AYA', 'AYAS MAHALLESİ'), ('DEV', 'DEVRİŞİYE MAHALLESİ'), ('KEM', 'KEMALPAŞA MAHALLESİ'), ('ÖRE', 'ÖREN MAHALLESİ'), ('ALİ', 'ALİTAŞI MAHALLESİ'), ('ALT', 'ALTINŞEHİR MAHALLESİ'), ('BAH', 'BAHÇECİK MAHALLESİ'), ('BAH', 'BAHÇELİEVLER MAHALLESİ'), ('BAR', 'BARBAROS HAYRETTİN MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('ESK', 'ESKİSARAY MAHALLESİ'), ('FAT', 'FATİH MAHALLESİ'), ('HOC', 'HOCAÖMER MAHALLESİ'), ('İMA', 'İMAMAĞA MAHALLESİ'), ('KAP', 'KAPCAMİ MAHALLESİ'), ('KAR', 'KARAPINAR MAHALLESİ'), ('KAY', 'KAYALIK MAHALLESİ'), ('MAL', 'MALAZGİRT MAHALLESİ'), ('MAR', 'MARA MAHALLESİ'), ('MEH', 'MEHMET AKİF MAHALLESİ'), ('MİM', 'MİMAR SİNAN MAHALLESİ'), ('MUS', 'MUSALLA MAHALLESİ'), ('ÖRE', 'ÖRENLİ MAHALLESİ'), ('TÜR', 'TÜRKİYE PETROLLERİ MAHALLESİ'), ('SIR', 'SIRATUT MAHALLESİ'), ('SİT', 'SİTELER MAHALLESİ'), ('SÜM', 'SÜMEREVLER MAHALLESİ'), ('TUR', 'TURGUT REİS MAHALLESİ'), ('ULU', 'ULUCAMİ MAHALLESİ'), ('VAR', 'VARLIK MAHALLESİ'), ('YAV', 'YAVUZ SELİM MAHALLESİ'), ('YEN', 'YENİ MAHALLESİ'), ('YEN', 'YENİ SANAYİ MAHALLESİ'), ('YEN', 'YENİPINAR MAHALLESİ'), ('YEŞ', 'YEŞİLYURT MAHALLESİ'), ('YUN', 'YUNUS EMRE MAHALLESİ'), ('ESE', 'ESENTEPE MAHALLESİ'), ('PET', 'PETROLOSB MAHALLESİ'), ('HAS', 'HASANCIK KÖYÜ, ATATÜRK MEVKİİ'), ('HAS', 'HASANCIK KÖYÜ, İNÖNÜ MEVKİİ'), ('HAS', 'HASANCIK KÖYÜ, TEPEBAŞI MEVKİİ'), ('YAY', 'YAYLAKONAK BELDESİ, ÇATDERESİ MAHALLESİ'), ('YAY', 'YAYLAKONAK BELDESİ, ÇİMENKE MAHALLESİ'), ('YAY', 'YAYLAKONAK BELDESİ, İNCEKOZ MAHALLESİ'), ('YAY', 'YAYLAKONAK BELDESİ, KARAÇALI MAHALLESİ'), ('YAY', 'YAYLAKONAK BELDESİ, MERKEZ MAHALLESİ'), ('YAY', 'YAYLAKONAK BELDESİ, ZİVAR MAHALLESİ'), ('ATA', 'ATAKENT KÖYÜ, ÜRGÜÇ MEVKİİ'), ('ATA', 'ATAKENT KÖYÜ, ATATÜRK MEVKİİ'), ('ATA', 'ATAKENT KÖYÜ, CUMHURİYET MEVKİİ'), ('ATA', 'ATAKENT KÖYÜ, VALİ HALİL IŞIK MEVKİİ'), ('ATA', 'ATAKENT KÖYÜ, BALABAN MEVKİİ'), ('ATA', 'ATAKENT KÖYÜ, BÜYÜK BOYALI  MEVKİİ'), ('KÖM', 'KÖMÜR BELDESİ, CUMHURİYET MAHALLESİ'), ('KÖM', 'KÖMÜR BELDESİ, ESENCE MAHALLESİ'), ('KÖM', 'KÖMÜR BELDESİ, HASANKAN MAHALLESİ'), ('KÖM', 'KÖMÜR BELDESİ, HÜRRİYET MAHALLESİ'), ('KÖM', 'KÖMÜR BELDESİ, SERİNTEPE MAHALLESİ'), ('KÖM', 'KÖMÜR BELDESİ, YAKACIK MAHALLESİ'), ('KÖM', 'KÖMÜR BELDESİ, YEŞİLYURT MAHALLESİ'), ('KÖM', 'KÖMÜR BELDESİ, BAHÇELİEVLER MAHALLESİ'), ('AŞA', 'AŞAĞISARHAN MAHALLESİ'), ('CİR', 'CİRİT MEYDANI MAHALLESİ'), ('ÇAT', 'ÇAT MAHALLESİ'), ('DUM', 'DUMLUPINAR MAHALLESİ'), ('ERD', 'ERDEMOĞLU MAHALLESİ'), ('KAY', 'KAYMAKAM HASAN TÜTÜN MAHALLESİ'), ('KOR', 'KORUPINAR MAHALLESİ'), ('PIN', 'PINARBAŞI MAHALLESİ'), ('YEN', 'YENİ BESNİ MAHALLESİ'), ('YUK', 'YUKARI SARHAN MAHALLESİ'), ('PIN', 'PINARBAŞIOSB MAHALLESİ'), ('SUG', 'SUGÖZÜ KÖYÜ, ATATÜRK MEVKİİ'), ('SUG', 'SUGÖZÜ KÖYÜ, İNÖNÜ MEVKİİ'), ('SAR', 'SARIYAPRAK KÖYÜ, CUMHURİYET MEVKİİ'), ('SAR', 'SARIYAPRAK KÖYÜ, FATİH MEVKİİ'), ('ÜÇG', 'ÜÇGÖZ KÖYÜ, ATATÜRK MEVKİİ'), ('ÜÇG', 'ÜÇGÖZ KÖYÜ, CUMHURRİYET MEVKİİ'), ('ÜÇG', 'ÜÇGÖZ KÖYÜ, İNÖNÜ MEVKİİ'), ('ÇAK', 'ÇAKIRHÜYÜK BELDESİ, ABIMISTIK MAHALLESİ'), ('ÇAK', 'ÇAKIRHÜYÜK BELDESİ, BOYBEYPINARI MAHALLESİ'), ('ÇAK', 'ÇAKIRHÜYÜK BELDESİ, KÖPRÜBAŞI MAHALLESİ'), ('ÇAK', 'ÇAKIRHÜYÜK BELDESİ, LEVZİN MAHALLESİ'), ('ÇAK', 'ÇAKIRHÜYÜK BELDESİ, YEŞİLOVA MAHALLESİ'), ('KES', 'KESMETEPE BELDESİ, ATATÜRK MAHALLESİ'), ('KES', 'KESMETEPE BELDESİ, ÇAKMAK MAHALLESİ'), ('KES', 'KESMETEPE BELDESİ, FATİH MAHALLESİ'), ('KES', 'KESMETEPE BELDESİ, İNCE MAHALLESİ'), ('KÖS', 'KÖSECELİ BELDESİ, CUMHURİYET MAHALLESİ'), ('KÖS', 'KÖSECELİ BELDESİ, HÜRRİYET MAHALLESİ'), ('KÖS', 'KÖSECELİ BELDESİ, TETİRLİ MAHALLESİ'), ('SUV', 'SUVARLI BELDESİ, ADALET MAHALLESİ'), ('SUV', 'SUVARLI BELDESİ, CUMHURİYET MAHALLESİ'), ('SUV', 'SUVARLI BELDESİ, HÜRRİYET MAHALLESİ'), ('ŞAM', 'ŞAMBAYAT BELDESİ, BAYAT MAHALLESİ'), ('ŞAM', 'ŞAMBAYAT BELDESİ, CUMHURİYET MAHALLESİ'), ('ŞAM', 'ŞAMBAYAT BELDESİ, FATİH MAHALLESİ'), ('ŞAM', 'ŞAMBAYAT BELDESİ, MENDERES MAHALLESİ'), ('ŞAM', 'ŞAMBAYAT BELDESİ, YENİ MAHALLESİ'), ('BAŞ', 'BAŞPINAR MAHALLESİ'), ('CAM', 'CAMİ MAHALLESİ'), ('YUN', 'YUNUS EMRE MAHALLESİ'), ('MAH', 'MAHMUT NEDİM ÖKMEN MAHALLESİ'), ('MER', 'MERKEZ MAHALLESİ'), ('ZAF', 'ZAFER MAHALLESİ'), ('BAH', 'BAHÇELİ EVLER MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('FAT', 'FATİH MAHALLESİ'), ('PIN', 'PINARBAŞI BELDESİ, AKTAŞ MAHALLESİ'), ('PIN', 'PINARBAŞI BELDESİ, BALIKBURUN MAHALLESİ'), ('PIN', 'PINARBAŞI BELDESİ, CAMİ MAHALLESİ'), ('PIN', 'PINARBAŞI BELDESİ, ÇAMLIYAYLA MAHALLESİ'), ('PIN', 'PINARBAŞI BELDESİ, HACILAR MAHALLESİ'), ('PIN', 'PINARBAŞI BELDESİ, İNÖNÜ MAHALLESİ'), ('PIN', 'PINARBAŞI BELDESİ, KAYA MAHALLESİ'), ('PIN', 'PINARBAŞI BELDESİ, KURUDERE MAHALLESİ'), ('FAT', 'FATİH MAHALLESİ'), ('KEL', 'KELEŞAN MAHALLESİ'), ('MER', 'MERKEZ MAHALLESİ'), ('YEN', 'YENİ MAHALLESİ'), ('ASF', 'ASFALT MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('FAT', 'FATİH MAHALLESİ'), ('HÜR', 'HÜRRİYET MAHALLESİ'), ('KUR', 'KURUGEÇİT MAHALLESİ'), ('MİM', 'MİMAR SİNAN MAHALLESİ'), ('YAV', 'YAVUZ SELİM MAHALLESİ'), ('YEN', 'YENİ MAHALLESİ'), ('BAL', 'BALKAR BELDESİ, ASFALT MAHALLESİ'), ('BAL', 'BALKAR BELDESİ, CUMHURİYET MAHALLESİ'), ('BEL', 'BELÖREN BELDESİ, CUMHURİYET MAHALLESİ'), ('BEL', 'BELÖREN BELDESİ, MERKEZ MAHALLESİ'), ('HAR', 'HARMANLI BELDESİ, CUMHURİYET MAHALLESİ'), ('HAR', 'HARMANLI BELDESİ, ÇAKMAK MAHALLESİ'), ('HAR', 'HARMANLI BELDESİ, KALEMKAS MAHALLESİ'), ('HAR', 'HARMANLI BELDESİ, YENİ MAHALLESİ'), ('ATA', 'ATATÜRK MAHALLESİ'), ('BAĞ', 'BAĞLAR MAHALLESİ'), ('BAY', 'BAYRAKTAR MAHALLESİ'), ('CAM', 'CAMİ MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('ÇOB', 'ÇOBANLI MAHALLESİ'), ('FAT', 'FATİH MAHALLESİ'), ('FIR', 'FIRAT MAHALLESİ'), ('GAZ', 'GAZİ MAHALLESİ'), ('GİR', 'GİRNE MAHALLESİ'), ('HÜR', 'HÜRRİYET MAHALLESİ'), ('KAR', 'KARŞIYAKA MAHALLESİ'), ('MEN', 'MENDERES MAHALLESİ'), ('ŞEY', 'ŞEYHBABA MAHALLESİ'), ('TUR', 'TURGUT ÖZAL MAHALLESİ'), ('YAV', 'YAVUZ SELİM MAHALLESİ'), ('YEN', 'YENİ MAHALLESİ'), ('BÖL', 'BÖLÜKYAYLA BELDESİ, ATATÜRK MAHALLESİ'), ('BÖL', 'BÖLÜKYAYLA BELDESİ, CUMHURİYET MAHALLESİ'), ('BÖL', 'BÖLÜKYAYLA BELDESİ, FATİH MAHALLESİ'), ('BÖL', 'BÖLÜKYAYLA BELDESİ, KANGÜLÜ MAHALLESİ'), ('AKI', 'AKINCILAR BELDESİ, KILAVUZ MAHALLESİ'), ('AKI', 'AKINCILAR BELDESİ, ÇAMLICA MAHALLESİ'), ('AKI', 'AKINCILAR BELDESİ, AKINCILAR ATATÜRK MAHALLESİ'), ('AKI', 'AKINCILAR BELDESİ, SOĞUKSU MAHALLESİ'), ('KAL', 'KALE MAHALLESİ'), ('ÖRE', 'ÖRENTAŞ MAHALLESİ'), ('YAV', 'YAVUZ SELİM MAHALLESİ'), ('AYE', 'AYENGİN MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('FAT', 'FATİH MAHALLESİ'), ('KAR', 'KARAMAN MAHALLESİ'), ('ONU', 'ONUR MAHALLESİ'), ('ZEY', 'ZEYNEL ASLAN MAHALLESİ'), ('MAH', 'MAHMUTOĞLU MAHALLESİ'), ('İNL', 'İNLİCE BELDESİ, ÇINAR MAHALLESİ'), ('İNL', 'İNLİCE BELDESİ, ÇÜKAN MAHALLESİ'), ('İNL', 'İNLİCE BELDESİ, FIRAT MAHALLESİ'), ('İNL', 'İNLİCE BELDESİ, KARADAĞ MAHALLESİ'), ('İNL', 'İNLİCE BELDESİ, ÖZBİLGİN MAHALLESİ'), ('İNL', 'İNLİCE BELDESİ, TAŞLICA MAHALLESİ'), ('İNL', 'İNLİCE BELDESİ, TUNA MAHALLESİ'), ('AYN', 'AYNİYE MAHALLESİ'), ('BUL', 'BULANIK MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('ÇAM', 'ÇAMLICA MAHALLESİ'), ('FET', 'FETHİYE MAHALLESİ'), ('REŞ', 'REŞADİYE MAHALLESİ'), ('SAL', 'SALAH MAHALLESİ'), ('AKM', 'AKMESCİT MAHALLESİ'), ('ALİ', 'ALİ ÇETİNKAYA MAHALLESİ'), ('ALİ', 'ALİ İHSAN PAŞA MAHALLESİ'), ('BAT', 'BATTALGAZİ MAHALLESİ'), ('BEY', 'BEYAZIT MAHALLESİ'), ('BUR', 'BURMALI MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('DAİ', 'DAİRECEP MAHALLESİ'), ('DER', 'DERVİŞ PAŞA MAHALLESİ'), ('DUM', 'DUMLUPINAR MAHALLESİ'), ('ERT', 'ERTUĞRUL GAZİ MAHALLESİ'), ('ESE', 'ESENTEPE MAHALLESİ'), ('EŞR', 'EŞREFPAŞA MAHALLESİ'), ('FAK', 'FAKIPAŞA MAHALLESİ'), ('FAT', 'FATİH MAHALLESİ'), ('GAZ', 'GAZİ MAHALLESİ'), ('GÜV', 'GÜVENEVLER MAHALLESİ'), ('HAM', 'HAMİDİYE MAHALLESİ'), ('HAS', 'HASAN KARAAĞAÇ MAHALLESİ'), ('HAT', 'HATTAT KARAHİSAR MAHALLESİ'), ('HOC', 'HOCA AHMET YESEVİ MAHALLESİ'), ('İST', 'İSTİKLAL MAHALLESİ'), ('KAN', 'KANLICA MAHALLESİ'), ('KAR', 'KARAMAN MAHALLESİ'), ('KAR', 'KARŞIYAKA MAHALLESİ'), ('KAS', 'KASIMPAŞA MAHALLESİ'), ('KAY', 'KAYADİBİ MAHALLESİ'), ('KOC', 'KOCATEPE MAHALLESİ'), ('MAR', 'MAREŞAL FEVZİ ÇAKMAK MAHALLESİ'), ('MAR', 'MARULCU MAHALLESİ'), ('MEC', 'MECİDİYE MAHALLESİ'), ('NAZ', 'NAZMİ SAATÇİ MAHALLESİ'), ('OLU', 'OLUCAK MAHALLESİ'), ('ORH', 'ORHANGAZİ MAHALLESİ'), ('OSM', 'OSMAN GAZİ MAHALLESİ'), ('ÖRN', 'ÖRNEKEVLER MAHALLESİ'), ('SAH', 'SAHİPATA MAHALLESİ'), ('SEL', 'SELÇUKLU MAHALLESİ'), ('SÜM', 'SÜMER MAHALLESİ'), ('TAC', 'TACI AHMET MAHALLESİ'), ('TAŞ', 'TAŞPINAR MAHALLESİ'), ('VEY', 'VEYSEL KARANİ MAHALLESİ'), ('YAR', 'YARENLER MAHALLESİ'), ('YEN', 'YENİCE MAHALLESİ'), ('YEŞ', 'YEŞİLYURT MAHALLESİ'), ('YUN', 'YUNUS EMRE MAHALLESİ'), ('ZAF', 'ZAFER MAHALLESİ'), ('AFY', 'AFYONKARAHİSAR OSB MAHALLESİ'), ('ANI', 'ANITKAYA KÖYÜ, CUMHURİYET MEVKİİ'), ('ANI', 'ANITKAYA KÖYÜ, ZAFER MEVKİİ'), ('BEY', 'BEYYAZI BELDESİ, ATATÜRK MAHALLESİ'), ('BEY', 'BEYYAZI BELDESİ, CUMHURİYET MAHALLESİ'), ('BEY', 'BEYYAZI BELDESİ, ÖRNEK MAHALLESİ'), ('KOC', 'KOCATEPE BELDESİ, KOCATEPE MAHALLESİ'), ('KOC', 'KOCATEPE BELDESİ, KURTULUŞ MAHALLESİ'), ('ÇAY', 'ÇAYIRBAĞ BELDESİ, ALİ ÇETİNKAYA MAHALLESİ'), ('ÇAY', 'ÇAYIRBAĞ BELDESİ, FATİH MAHALLESİ'), ('ÇAY', 'ÇAYIRBAĞ BELDESİ, HUZUR MAHALLESİ'), ('ÇAY', 'ÇAYIRBAĞ BELDESİ, UĞUR MAHALLESİ'), ('ÇIK', 'ÇIKRIK BELDESİ, ERENLER MAHALLESİ'), ('ÇIK', 'ÇIKRIK BELDESİ, YUNUSLAR MAHALLESİ'), ('DEĞ', 'DEĞİRMENAYVALI BELDESİ, KURTULUŞ MAHALLESİ'), ('DEĞ', 'DEĞİRMENAYVALI BELDESİ, ŞEHİT AHMET MAHALLESİ'), ('ERK', 'ERKMEN BELDESİ, CUMHURİYET MAHALLESİ'), ('ERK', 'ERKMEN BELDESİ, FEVZİ ÇAKMAK MAHALLESİ'), ('ERK', 'ERKMEN BELDESİ, HÜRRİYET MAHALLESİ'), ('FET', 'FETHİBEY BELDESİ, FATİH MAHALLESİ'), ('FET', 'FETHİBEY BELDESİ, YAVUZ SELİM MAHALLESİ'), ('FET', 'FETHİBEY BELDESİ, YUNUS EMRE MAHALLESİ'), ('GEB', 'GEBECELER BELDESİ, FATİH MAHALLESİ'), ('GEB', 'GEBECELER BELDESİ, İSTİKLAL MAHALLESİ'), ('GEB', 'GEBECELER BELDESİ, KOCATEPE MAHALLESİ'), ('GEB', 'GEBECELER BELDESİ, ZAFER MAHALLESİ'), ('GEB', 'GEBECELER BELDESİ, YENİ MAHALLESİ'), ('IŞI', 'IŞIKLAR BELDESİ, ATATÜRK MAHALLESİ'), ('IŞI', 'IŞIKLAR BELDESİ, CUMHURİYET MAHALLESİ'), ('IŞI', 'IŞIKLAR BELDESİ, HÜRRİYET MAHALLESİ'), ('IŞI', 'IŞIKLAR BELDESİ, İSTİKLAL MAHALLESİ'), ('IŞI', 'IŞIKLAR BELDESİ, YAKA MAHALLESİ'), ('IŞI', 'IŞIKLAR BELDESİ, YENİ MAHALLESİ'), ('NUR', 'NURİBEY BELDESİ, ALİ İHSAN PAŞA MAHALLESİ'), ('NUR', 'NURİBEY BELDESİ, FATİH MAHALLESİ'), ('NUR', 'NURİBEY BELDESİ, MAREŞAL FEVZİ ÇAKMAK MAHALLESİ'), ('NUR', 'NURİBEY BELDESİ, MEHMET AKİF MAHALLESİ'), ('SAL', 'SALAR BELDESİ, BARBAROS MAHALLESİ'), ('SAL', 'SALAR BELDESİ, FATİH MAHALLESİ'), ('SAL', 'SALAR BELDESİ, HALİL İBRAHİM SULTAN MAHALLESİ'), ('SAL', 'SALAR BELDESİ, YAVUZ SELİM MAHALLESİ'), ('SAL', 'SALAR BELDESİ, GÜMÜŞ TEPE MAHALLESİ'), ('SUS', 'SUSUZ BELDESİ, GÖKHAN MAHALLESİ'), ('SUS', 'SUSUZ BELDESİ, OSMANLI MAHALLESİ'), ('SUS', 'SUSUZ BELDESİ, SAKARYA MAHALLESİ'), ('SUS', 'SUSUZ BELDESİ, SELÇUKLU MAHALLESİ'), ('SÜL', 'SÜLÜMENLİ BELDESİ, ALTINDAĞ MAHALLESİ'), ('SÜL', 'SÜLÜMENLİ BELDESİ, CUMHURİYET MAHALLESİ'), ('SÜL', 'SÜLÜMENLİ BELDESİ, İSTİKLAL MAHALLESİ'), ('SÜL', 'SÜLÜMENLİ BELDESİ, ŞEKER MAHALLESİ'), ('SÜL', 'SÜLÜMENLİ BELDESİ, ULUCAMİ MAHALLESİ'), ('SÜL', 'SÜLÜMENLİ BELDESİ, ZAFER MAHALLESİ'), ('SÜL', 'SÜLÜN BELDESİ, GÜLTEPE MAHALLESİ'), ('SÜL', 'SÜLÜN BELDESİ, HİSAR MAHALLESİ'), ('AŞA', 'AŞAĞI HİLAL MAHALLESİ'), ('BAR', 'BARBAROS MAHALLESİ'), ('ÇAĞ', 'ÇAĞLAYAN MAHALLESİ'), ('FAT', 'FATİH MAHALLESİ'), ('GÜL', 'GÜLİSTAN MAHALLESİ'), ('MİM', 'MİMAR SİNAN MAHALLESİ'), ('YEN', 'YENİ MAHALLESİ'), ('YUK', 'YUKARI HİLAL MAHALLESİ'), ('YAK', 'YAKA KÖYÜ, AŞAĞI MEVKİİ'), ('YAK', 'YAKA KÖYÜ, YUKARI MEVKİİ'), ('BÜY', 'BÜYÜK MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('HÜR', 'HÜRRİYET MAHALLESİ'), ('YEN', 'YENİ MAHALLESİ'), ('AKÇ', 'AKÇEŞME MAHALLESİ'), ('ALA', 'ALACA MAHALLESİ'), ('ALİ', 'ALİ EFENDİ MAHALLESİ'), ('AŞA', 'AŞAĞI GÖKÇEYAYLA MAHALLESİ'), ('AYD', 'AYDINLAR MAHALLESİ'), ('BAD', 'BADEMLİ MAHALLESİ'), ('BAĞ', 'BAĞLARBAŞI MAHALLESİ'), ('BAĞ', 'BAĞLARÜSTÜ MAHALLESİ'), ('BAH', 'BAHÇELİEVLER MAHALLESİ'), ('BEK', 'BEKİR AĞA MAHALLESİ'), ('BUC', 'BUCAK MAHALLESİ'), ('CİR', 'CİRİT MAHALLESİ'), ('ÇAR', 'ÇARDAKLI MAHALLESİ'), ('EMR', 'EMRULLAH MAHALLESİ'), ('ERK', 'ERKMEN MAHALLESİ'), ('FAT', 'FATİH MAHALLESİ'), ('GÖL', 'GÖLBAŞI MAHALLESİ'), ('HAC', 'HACI ESAT MAHALLESİ'), ('HAC', 'HACI HALİFE MAHALLESİ'), ('HAC', 'HACI ÖMER MAHALLESİ'), ('HAC', 'HACI YUSUF MAHALLESİ'), ('HAS', 'HASTANE MAHALLESİ'), ('HİS', 'HİSAR MAHALLESİ'), ('İHS', 'İHSANİYE MAHALLESİ'), ('İMA', 'İMARET MAHALLESİ'), ('KAL', 'KALE MAHALLESİ'), ('KAR', 'KARABAĞLAR MAHALLESİ'), ('KAY', 'KAYMAZ MAHALLESİ'), ('KES', 'KESTEMET MAHALLESİ'), ('KIR', 'KIRKGÖZ MAHALLESİ'), ('KIR', 'KIRKLAR MAHALLESİ'), ('KON', 'KONAK MAHALLESİ'), ('LAL', 'LALA SİNAN PAŞA MAHALLESİ'), ('MAL', 'MALAZGİRT MAHALLESİ'), ('MES', 'MESCİT MAHALLESİ'), ('MÜS', 'MÜSLÜMANA MAHALLESİ'), ('ÖME', 'ÖMEROĞLU MAHALLESİ'), ('SEL', 'SELÇUKLU MAHALLESİ'), ('SÜL', 'SÜLEYMANİYE MAHALLESİ'), ('ŞAZ', 'ŞAZİ MAHALLESİ'), ('ŞIH', 'ŞIHLAR MAHALLESİ'), ('TAŞ', 'TAŞAĞIL MAHALLESİ'), ('YAK', 'YAKUP ŞEVKİ PAŞA MAHALLESİ'), ('YEN', 'YENİ MAHALLESİ'), ('YEN', 'YENİ DOĞAN MAHALLESİ'), ('YEN', 'YENİCE MAHALLESİ'), ('YIL', 'YILDIRIM MAHALLESİ'), ('YUK', 'YUKARI GÖKÇEYAYLA MAHALLESİ'), ('ETH', 'ETHEM KELEKÇİ MAHALLESİ'), ('BÜY', 'BÜYÜKKARABAĞ KÖYÜ, ATATÜRK MEVKİİ'), ('BÜY', 'BÜYÜKKARABAĞ KÖYÜ, HACIBEKİR MEVKİİ'), ('BÜY', 'BÜYÜKKARABAĞ KÖYÜ, KARŞIYAKA MEVKİİ'), ('BÜY', 'BÜYÜKKARABAĞ KÖYÜ, FEVZİÇAKMAK MEVKİİ'), ('DİŞ', 'DİŞLİ BELDESİ, ÇAYBAŞI MAHALLESİ'), ('DİŞ', 'DİŞLİ BELDESİ, FATİH MAHALLESİ'), ('DİŞ', 'DİŞLİ BELDESİ, KÖPRÜBAŞI MAHALLESİ'), ('DİŞ', 'DİŞLİ BELDESİ, MALAZGİRT MAHALLESİ'), ('DİŞ', 'DİŞLİ BELDESİ, MEVLANA MAHALLESİ'), ('DİŞ', 'DİŞLİ BELDESİ, OKUL MAHALLESİ'), ('DİŞ', 'DİŞLİ BELDESİ, ŞEYH ŞAMİL MAHALLESİ'), ('DİŞ', 'DİŞLİ BELDESİ, YAVUZ SELİM MAHALLESİ'), ('DİŞ', 'DİŞLİ BELDESİ, YUKARI MAHALLESİ'), ('DİŞ', 'DİŞLİ BELDESİ, YUNUS EMRE MAHALLESİ'), ('KEM', 'KEMERKAYA KÖYÜ, AVDAN MEVKİİ'), ('KEM', 'KEMERKAYA KÖYÜ, HÜRRİYET MEVKİİ'), ('KEM', 'KEMERKAYA KÖYÜ, SAVAŞ MEVKİİ'), ('KEM', 'KEMERKAYA KÖYÜ, YAKA MEVKİİ'), ('KEM', 'KEMERKAYA KÖYÜ, YAPRAKLI MEVKİİ'), ('KEM', 'KEMERKAYA KÖYÜ, YENİ MEVKİİ'), ('KEM', 'KEMERKAYA KÖYÜ, ZAFER MEVKİİ'), ('ÖZB', 'ÖZBURUN BELDESİ, BAHÇELİEVLER MAHALLESİ'), ('ÖZB', 'ÖZBURUN BELDESİ, ÇAYBAŞI MAHALLESİ'), ('ÖZB', 'ÖZBURUN BELDESİ, ŞEHİRÖNÜ MAHALLESİ'), ('ÖZB', 'ÖZBURUN BELDESİ, ULUCAMİ MAHALLESİ'), ('ÖZB', 'ÖZBURUN BELDESİ, ÜSKÜDAR MAHALLESİ'), ('AKT', 'AKTAŞ MAHALLESİ'), ('ALİ', 'ALİ İHSAN PAŞA MAHALLESİ'), ('ALİ', 'ALİ KALELİ MAHALLESİ'), ('AŞA', 'AŞAĞI MAHALLESİ'), ('BAH', 'BAHÇELİEVLER MAHALLESİ'), ('CED', 'CEDİT MAHALLESİ'), ('DEM', 'DEMİRAĞAÇ MAHALLESİ'), ('DUM', 'DUMLUPINAR MAHALLESİ'), ('İST', 'İSTASYON MAHALLESİ'), ('KÖP', 'KÖPRÜBAŞI MAHALLESİ'), ('ORT', 'ORTA MAHALLESİ'), ('ŞİR', 'ŞİRİNEVLER MAHALLESİ'), ('TEK', 'TEKKE MAHALLESİ'), ('VAK', 'VAKIF MAHALLESİ'), ('YAK', 'YAKA MAHALLESİ'), ('AKK', 'AKKONAK KÖYÜ, AKHÜRREM MEVKİİ'), ('AKK', 'AKKONAK KÖYÜ, BALTACI MEVKİİ'), ('AKK', 'AKKONAK KÖYÜ, CUMHURİYET MEVKİİ'), ('AKK', 'AKKONAK KÖYÜ, HÜRRİYET MEVKİİ'), ('AKK', 'AKKONAK KÖYÜ, MİLLİ EGEMENLİK MEVKİİ'), ('DER', 'DERESİNEK KÖYÜ, GÜNDOĞDU MEVKİİ'), ('DER', 'DERESİNEK KÖYÜ, KAHRAMAN MEVKİİ'), ('DER', 'DERESİNEK KÖYÜ, ZAFER MEVKİİ'), ('EBE', 'EBER KÖYÜ, ORTA MEVKİİ'), ('EBE', 'EBER KÖYÜ, TEKKE MEVKİİ'), ('EBE', 'EBER KÖYÜ, YENİ MEVKİİ'), ('EBE', 'EBER KÖYÜ, YUKARI MEVKİİ'), ('İNL', 'İNLİ KÖYÜ, ALPASLAN MEVKİİ'), ('İNL', 'İNLİ KÖYÜ, CUMHURİYET MEVKİİ'), ('İNL', 'İNLİ KÖYÜ, EVREN MEVKİİ'), ('İNL', 'İNLİ KÖYÜ, KAVAKLI MEVKİİ'), ('İNL', 'İNLİ KÖYÜ, KOCATEPE MEVKİİ'), ('İNL', 'İNLİ KÖYÜ, YAYLA MEVKİİ'), ('KAR', 'KARAMIK KÖYÜ, CUMHURİYET MEVKİİ'), ('KAR', 'KARAMIK KÖYÜ, 75. YIL MEVKİİ'), ('KAR', 'KARAMIKKARACAÖREN BELDESİ, AŞAĞI MAHALLESİ'), ('KAR', 'KARAMIKKARACAÖREN BELDESİ, BAĞLAR MAHALLESİ'), ('KAR', 'KARAMIKKARACAÖREN BELDESİ, SEKA MAHALLESİ'), ('KAR', 'KARAMIKKARACAÖREN BELDESİ, YUKARI MAHALLESİ'), ('KOÇ', 'KOÇBEYLİ KÖYÜ, GÖÇMEZLER MEVKİİ'), ('KOÇ', 'KOÇBEYLİ KÖYÜ, GÜLBAHARLI MEVKİİ'), ('KOÇ', 'KOÇBEYLİ KÖYÜ, AŞAĞI MEVKİİ'), ('KOÇ', 'KOÇBEYLİ KÖYÜ, YENİ MEVKİİ'), ('PAZ', 'PAZARAĞAÇ BELDESİ, AFYON MAHALLESİ'), ('PAZ', 'PAZARAĞAÇ BELDESİ, BEŞEVLER MAHALLESİ'), ('PAZ', 'PAZARAĞAÇ BELDESİ, KARABULUT MAHALLESİ'), ('PAZ', 'PAZARAĞAÇ BELDESİ, ORTA MAHALLESİ'), ('PAZ', 'PAZARAĞAÇ BELDESİ, YUKARI MAHALLESİ'), ('BUC', 'BUCAK MAHALLESİ'), ('IŞI', 'IŞIK MAHALLESİ'), ('KAR', 'KARADEDE MAHALLESİ'), ('SIR', 'SIRAKAPI MAHALLESİ'), ('YEN', 'YENİ MAHALLESİ'), ('ZAF', 'ZAFER MAHALLESİ'), ('KOC', 'KOCAÖZ BELDESİ, ATATÜRK MAHALLESİ'), ('KOC', 'KOCAÖZ BELDESİ, FATİH MAHALLESİ'), ('KOC', 'KOCAÖZ BELDESİ, İSTİKLAL MAHALLESİ'), ('KOC', 'KOCAÖZ BELDESİ, CUMHURİYET MAHALLESİ'), ('BAR', 'BARBAROS MAHALLESİ'), ('ÇAM', 'ÇAMLIK MAHALLESİ'), ('ESE', 'ESENTEPE MAHALLESİ'), ('KUR', 'KURTULUŞ MAHALLESİ'), ('YEN', 'YENİYOL MAHALLESİ'), ('YEŞ', 'YEŞİLYURT MAHALLESİ'), ('VEH', 'VEHBİ KOÇ SANAYİ BÖLGESİ MAHALLESİ'), ('YÜR', 'YÜREĞİL KÖYÜ, DEMİREL MEVKİİ'), ('YÜR', 'YÜREĞİL KÖYÜ, FATİH MEVKİİ'), ('ADL', 'ADLİYE MAHALLESİ'), ('ALT', 'ALTMIŞEVLER MAHALLESİ'), ('ATA', 'ATATÜRK MAHALLESİ'), ('BAĞ', 'BAĞLAR MAHALLESİ'), ('CAM', 'CAMİKEBİR MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('GAZ', 'GAZİ MEHMET ÇAVUŞ MAHALLESİ'), ('DÖR', 'DÖRTYOL MAHALLESİ'), ('EMN', 'EMNİYET MAHALLESİ'), ('HÜR', 'HÜRRİYET MAHALLESİ'), ('ILI', 'ILICA MAHALLESİ'), ('İNC', 'İNCİRLİ MAHALLESİ'), ('İST', 'İSTASYON MAHALLESİ'), ('İTF', 'İTFAİYE MAHALLESİ'), ('KON', 'KONAK MAHALLESİ'), ('KOR', 'KORUBAŞI MAHALLESİ'), ('OTO', 'OTOGAR MAHALLESİ'), ('PAN', 'PANCAR MAHALLESİ'), ('PAZ', 'PAZAR MAHALLESİ'), ('PIN', 'PINARBAŞI MAHALLESİ'), ('SAN', 'SANAYİ MAHALLESİ'), ('SAN', 'SANTRAL MAHALLESİ'), ('STA', 'STADYUM MAHALLESİ'), ('SUÇ', 'SUÇIKAN MAHALLESİ'), ('TOP', 'TOPTEPE MAHALLESİ'), ('ÜÇL', 'ÜÇLERCE MAHALLESİ'), ('YEN', 'YENİ MAHALLESİ'), ('ULU', 'ULUKÖY KÖYÜ, CAMİKEBİR MEVKİİ'), ('ULU', 'ULUKÖY KÖYÜ, YENİ MEVKİİ'), ('HAY', 'HAYDARLI BELDESİ, CUMHURİYET MAHALLESİ'), ('HAY', 'HAYDARLI BELDESİ, HÜRRİYET MAHALLESİ'), ('HAY', 'HAYDARLI BELDESİ, İSTİKLAL MAHALLESİ'), ('HAY', 'HAYDARLI BELDESİ, MERKEZ MAHALLESİ'), ('HAY', 'HAYDARLI BELDESİ, ÖRNEK MAHALLESİ'), ('HAY', 'HAYDARLI BELDESİ, YENİ MAHALLESİ'), ('ÇİÇ', 'ÇİÇEKTEPE KÖYÜ, ALPASLAN MEVKİİ'), ('ÇİÇ', 'ÇİÇEKTEPE KÖYÜ, ATATÜRK MEVKİİ'), ('ÇİÇ', 'ÇİÇEKTEPE KÖYÜ, CUMHURİYET MEVKİİ'), ('ÇİÇ', 'ÇİÇEKTEPE KÖYÜ, FATİH MEVKİİ'), ('DOĞ', 'DOĞANLI KÖYÜ, CUMHURİYET MEVKİİ'), ('DOĞ', 'DOĞANLI KÖYÜ, GAZİ MEVKİİ'), ('DOĞ', 'DOĞANLI KÖYÜ, ÖRNEK MEVKİİ'), ('KAD', 'KADILAR KÖYÜ, ATATÜRK MEVKİİ'), ('KAD', 'KADILAR KÖYÜ, CUMHURİYET MEVKİİ'), ('KAD', 'KADILAR KÖYÜ, İNÖNÜ MEVKİİ'), ('KAD', 'KADILAR KÖYÜ, ZAFER MEVKİİ'), ('KIN', 'KINIK KÖYÜ, BAHÇELİEVLER MEVKİİ'), ('KIN', 'KINIK KÖYÜ, ESENTEPE MEVKİİ'), ('KIN', 'KINIK KÖYÜ, FATİH MEVKİİ'), ('KIN', 'KINIK KÖYÜ, ÖZTÜRK MEVKİİ'), ('TAT', 'TATARLI BELDESİ, ALTINHİSAR MAHALLESİ'), ('TAT', 'TATARLI BELDESİ, CUMHURİYET MAHALLESİ'), ('TAT', 'TATARLI BELDESİ, ÇAĞLAYAN MAHALLESİ'), ('TAT', 'TATARLI BELDESİ, ÇAMLICA MAHALLESİ'), ('TAT', 'TATARLI BELDESİ, FATİH MAHALLESİ'), ('TAT', 'TATARLI BELDESİ, YEŞİLYURT MAHALLESİ'), ('YIP', 'YIPRAK KÖYÜ, BAHÇELİEVLER MEVKİİ'), ('YIP', 'YIPRAK KÖYÜ, ESENTEPE MEVKİİ'), ('YIP', 'YIPRAK KÖYÜ, HİSAR MEVKİİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('ÇİL', 'ÇİLLİ MAHALLESİ'), ('ESK', 'ESKİ KACERLİ MAHALLESİ'), ('İNC', 'İNCİLİ MAHALLESİ'), ('İNK', 'İNKİLAP MAHALLESİ'), ('KAR', 'KARŞIYAKA MAHALLESİ'), ('MEN', 'MENDERES MAHALLESİ'), ('YEN', 'YENİ MAHALLESİ'), ('YEN', 'YENİ KACERLİ MAHALLESİ'), ('YEN', 'YENİDOĞAN MAHALLESİ'), ('ADA', 'ADAYAZI KÖYÜ, CUMHURİYET MEVKİİ'), ('ADA', 'ADAYAZI KÖYÜ, YENİ MEVKİİ'), ('ADA', 'ADAYAZI KÖYÜ, YENİDOĞAN MEVKİİ'), ('GÖM', 'GÖMÜ BELDESİ, BAĞLARBAŞI MAHALLESİ'), ('GÖM', 'GÖMÜ BELDESİ, DÖRTYOL MAHALLESİ'), ('GÖM', 'GÖMÜ BELDESİ, FATİH MAHALLESİ'), ('DAV', 'DAVULGA BELDESİ, SOFULU MAHALLESİ'), ('DAV', 'DAVULGA BELDESİ, ALASAKALLI MAHALLESİ'), ('DAV', 'DAVULGA BELDESİ, DOMURLU MAHALLESİ'), ('DAV', 'DAVULGA BELDESİ, İNCİK MAHALLESİ'), ('AŞA', 'AŞAĞIPİRİBEYLİ KÖYÜ, CUMHURİYET MEVKİİ'), ('AŞA', 'AŞAĞIPİRİBEYLİ KÖYÜ, KARŞIYAKA MEVKİİ'), ('AŞA', 'AŞAĞIPİRİBEYLİ KÖYÜ, YENİ MEVKİİ'), ('BAD', 'BADEMLİ KÖYÜ, ADALET MEVKİİ'), ('BAD', 'BADEMLİ KÖYÜ, YILDIZ MEVKİİ'), ('BAD', 'BADEMLİ KÖYÜ, ZAFER MEVKİİ'), ('CAM', 'CAMİKEBİR MAHALLESİ'), ('FAT', 'FATİH MAHALLESİ'), ('KAY', 'KAYALIK MAHALLESİ'), ('YUN', 'YUNUS EMRE MAHALLESİ'), ('GÖK', 'GÖKÇEK KÖYÜ, BARBAROS MEVKİİ'), ('GÖK', 'GÖKÇEK KÖYÜ, FATİH MEVKİİ'), ('HÜR', 'HÜRRİYET MAHALLESİ'), ('ŞAF', 'ŞAFAK MAHALLESİ'), ('YEN', 'YENİ MAHALLESİ'), ('YEŞ', 'YEŞİLHİSAR KÖYÜ, CUMHURİYET MEVKİİ'), ('YEŞ', 'YEŞİLHİSAR KÖYÜ, FATİH MEVKİİ'), ('YEŞ', 'YEŞİLHİSAR KÖYÜ, HİSAR MEVKİİ'), ('YEŞ', 'YEŞİLHİSAR KÖYÜ, YENİ MEVKİİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('HÜR', 'HÜRRİYET MAHALLESİ'), ('ŞAH', 'ŞAHİNLER MAHALLESİ'), ('ZAF', 'ZAFER MAHALLESİ'), ('AYA', 'AYAZİNİ KÖYÜ, CUMHURİYET MEVKİİ'), ('AYA', 'AYAZİNİ KÖYÜ, FATİH MEVKİİ'), ('BOZ', 'BOZHÜYÜK KÖYÜ, CUMHURİYET MEVKİİ'), ('BOZ', 'BOZHÜYÜK KÖYÜ, ŞEHİTLER MEVKİİ'), ('BOZ', 'BOZHÜYÜK KÖYÜ, YUNUS EMRE MEVKİİ'), ('DÖĞ', 'DÖĞER BELDESİ, FATİH MAHALLESİ'), ('DÖĞ', 'DÖĞER BELDESİ, KERVANSARAY MAHALLESİ'), ('DÖĞ', 'DÖĞER BELDESİ, YENİ MAHALLESİ'), ('DÖĞ', 'DÖĞER BELDESİ, YUNUS EMRE MAHALLESİ'), ('GAZ', 'GAZLIGÖL BELDESİ, BELCE MAHALLESİ'), ('GAZ', 'GAZLIGÖL BELDESİ, CUMHURİYET MAHALLESİ'), ('GAZ', 'GAZLIGÖL BELDESİ, FATİH MAHALLESİ'), ('GAZ', 'GAZLIGÖL BELDESİ, YUNUS EMRE MAHALLESİ'), ('KAR', 'KARACAAHMET KÖYÜ, CUMHURİYET MEVKİİ'), ('KAR', 'KARACAAHMET KÖYÜ, TÜRBE MEVKİİ'), ('KAY', 'KAYIHAN BELDESİ, CUMHURİYET MAHALLESİ'), ('KAY', 'KAYIHAN BELDESİ, KUNDUZLU MAHALLESİ'), ('KAY', 'KAYIHAN BELDESİ, PINAR MAHALLESİ'), ('KAY', 'KAYIHAN BELDESİ, TÜRBE MAHALLESİ'), ('YAY', 'YAYLABAĞI BELDESİ, ATATÜRK MAHALLESİ'), ('YAY', 'YAYLABAĞI BELDESİ, BAHÇELİEVLER MAHALLESİ'), ('YAY', 'YAYLABAĞI BELDESİ, ESENTEPE MAHALLESİ'), ('ÇUK', 'ÇUKUR MAHALLESİ'), ('ESE', 'ESENTEPE MAHALLESİ'), ('ESK', 'ESKİ HAMAM MAHALLESİ'), ('KAV', 'KAVAK MAHALLESİ'), ('MED', 'MEDRESE MAHALLESİ'), ('TEP', 'TEPECİK MAHALLESİ'), ('ZEY', 'ZEYBEK MAHALLESİ'), ('ŞİR', 'ŞİRİNEVLER MAHALLESİ'), ('FAT', 'FATİH MAHALLESİ'), ('SEL', 'SELÇUKLU MAHALLESİ'), ('MER', 'MERMER OSB MAHALLESİ'), ('ALA', 'ALANYURT KÖYÜ, ATATÜRK MEVKİİ'), ('ALA', 'ALANYURT KÖYÜ, CUMHURİYET MEVKİİ'), ('ALA', 'ALANYURT KÖYÜ, ÇAKMAK MEVKİİ'), ('ALA', 'ALANYURT KÖYÜ, HÜRRİYET MEVKİİ'), ('ALA', 'ALANYURT KÖYÜ, SELİMİYE MEVKİİ'), ('SEY', 'SEYDİLER BELDESİ, CUMHURİYET MAHALLESİ'), ('SEY', 'SEYDİLER BELDESİ, HASAN BASRİ MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('YEN', 'YENİ MAHALLESİ'), ('CUM', 'CUMA MAHALLESİ'), ('ÇAK', 'ÇAKIR MAHALLESİ'), ('ÇAY', 'ÇAY MAHALLESİ'), ('ECE', 'ECE MAHALLESİ'), ('HİS', 'HİSAR MAHALLESİ'), ('İST', 'İSTASYON MAHALLESİ'), ('ŞİR', 'ŞİRİNEVLER MAHALLESİ'), ('YUN', 'YUNUS EMRE MAHALLESİ'), ('BAL', 'BALLIK KÖYÜ, CUMHURİYET MEVKİİ'), ('BAL', 'BALLIK KÖYÜ, ESENTEPE MEVKİİ'), ('BAL', 'BALLIK KÖYÜ, ZAFER MEVKİİ'), ('KIZ', 'KIZIK KÖYÜ, GÜNEY MEVKİİ'), ('KIZ', 'KIZIK KÖYÜ, KUZEY MEVKİİ'), ('KIZ', 'KIZIK KÖYÜ, ORTA MEVKİİ'), ('KUS', 'KUSURA KÖYÜ, CUMHURİYET MEVKİİ'), ('KUS', 'KUSURA KÖYÜ, FATİH MEVKİİ'), ('KUS', 'KUSURA KÖYÜ, HÜRRİYET MEVKİİ'), ('MEN', 'MENTEŞ KÖYÜ, FATİH MEVKİİ'), ('MEN', 'MENTEŞ KÖYÜ, HÜRRİYET MEVKİİ'), ('ÖRE', 'ÖRENKAYA KÖYÜ, BAHÇELİ MEVKİİ'), ('ÖRE', 'ÖRENKAYA KÖYÜ, NUR MEVKİİ'), ('SOR', 'SORKUN KÖYÜ, EMEK MEVKİİ'), ('SOR', 'SORKUN KÖYÜ, KESTEL MEVKİİ'), ('SOR', 'SORKUN KÖYÜ, YÜKSELİŞ MEVKİİ'), ('YAV', 'YAVAŞLAR KÖYÜ, CUMHURİYET MEVKİİ'), ('YAV', 'YAVAŞLAR KÖYÜ, HİSAR MEVKİİ'), ('YAV', 'YAVAŞLAR KÖYÜ, KURTULUŞ MEVKİİ'), ('KAR', 'KARADİREK KÖYÜ, CUMHURİYET MEVKİİ'), ('KAR', 'KARADİREK KÖYÜ, HÜRRİYET MEVKİİ'), ('KAR', 'KARADİREK KÖYÜ, İSTİKLAL MEVKİİ'), ('AKH', 'AKHARIM BELDESİ, ÇİĞİLTEPE MAHALLESİ'), ('AKH', 'AKHARIM BELDESİ, DİKMEN MAHALLESİ'), ('AKH', 'AKHARIM BELDESİ, HİSAR MAHALLESİ'), ('BAŞ', 'BAŞAĞAÇ KÖYÜ, CUMHURİYET MEVKİİ'), ('BAŞ', 'BAŞAĞAÇ KÖYÜ, İSTİKLAL MEVKİİ'), ('BAŞ', 'BAŞAĞAÇ KÖYÜ, ŞAFAK MEVKİİ'), ('AKP', 'AKPINAR MAHALLESİ'), ('ALİ', 'ALİ ÇETİNKAYA MAHALLESİ'), ('BAH', 'BAHÇELİEVLER MAHALLESİ'), ('CUM', 'CUMHURİYET MAHALLESİ'), ('ÇİĞ', 'ÇİĞİLTEPE MAHALLESİ'), ('FAT', 'FATİH MAHALLESİ'), ('ÖĞR', 'ÖĞRETMENLER MAHALLESİ'), ('YUK', 'YUKARI MAHALLESİ'), ('AHM', 'AHMETPAŞA BELDESİ, ÇİĞİLTEPE MAHALLESİ'), ('AHM', 'AHMETPAŞA BELDESİ, DİBEKBAŞI MAHALLESİ'), ('AHM', 'AHMETPAŞA BELDESİ, GÖLCÜK MAHALLESİ'), ('AHM', 'AHMETPAŞA BELDESİ, HALKALI MAHALLESİ'), ('AHM', 'AHMETPAŞA BELDESİ, KÜÇÜKTEPE MAHALLESİ'), ('AHM', 'AHMETPAŞA BELDESİ, YUKARI MAHALLESİ'), ('AKÖ', 'AKÖREN BELDESİ, BAĞDAT MAHALLESİ'), ('AKÖ', 'AKÖREN BELDESİ, FATİH MAHALLESİ'), ('AKÖ', 'AKÖREN BELDESİ, YILDIRIM BEYAZIT MAHALLESİ'), ('DÜZ', 'DÜZAĞAÇ BELDESİ, CUMHURİYET MAHALLESİ'), ('DÜZ', 'DÜZAĞAÇ BELDESİ, FATİH MAHALLESİ'), ('DÜZ', 'DÜZAĞAÇ BELDESİ, IŞIK MAHALLESİ'), ('DÜZ', 'DÜZAĞAÇ BELDESİ, ZAFER MAHALLESİ'), ('GÜN', 'GÜNEY KÖYÜ, AŞAĞI MEVKİİ'), ('GÜN', 'GÜNEY KÖYÜ, ORTA MEVKİİ'), ('GÜN', 'GÜNEY KÖYÜ, YUKARI MEVKİİ'), ('GÜN', 'GÜNEY KÖYÜ, YENİ MEVKİİ'), ('KIL', 'KILIÇARSLAN BELDESİ, ATATÜRK MAHALLESİ'), ('KIL', 'KILIÇARSLAN BELDESİ, CUMHURİYET MAHALLESİ'), ('KIL', 'KILIÇARSLAN BELDESİ, FEVZİ ÇAKMAK MAHALLESİ'), ('KIL', 'KILIÇARSLAN BELDESİ, KOCATEPE MAHALLESİ'), ('KIR', 'KIRKA BELDESİ, ATATÜRK MAHALLESİ'), ('KIR', 'KIRKA BELDESİ, FATİH MAHALLESİ'), ('KIR', 'KIRKA BELDESİ, YAVUZ SULTAN SELİM MAHALLESİ'), ('KIR', 'KIRKA BELDESİ, YILDIRIM BEYAZIT MAHALLESİ'), ('KÜÇ', 'KÜÇÜKHÜYÜK BELDESİ, CUMHURİYET MAHALLESİ'), ('KÜÇ', 'KÜÇÜKHÜYÜK BELDESİ, FATİH MAHALLESİ'), ('KÜÇ', 'KÜÇÜKHÜYÜK BELDESİ, KURTULUŞ MAHALLESİ'), ('KÜÇ', 'KÜÇÜKHÜYÜK BELDESİ, ZAFER MAHALLESİ'), ('KÜÇ', 'KÜÇÜKHÜYÜK BELDESİ, ATATÜRK MAHALLESİ'), ('NUH', 'NUH KÖYÜ, BAHÇELİEVLER MEVKİİ'), ('NUH', 'NUH KÖYÜ, CUMHURİYET MEVKİİ'), ('NUH', 'NUH KÖYÜ, HÜRRİYET MEVKİİ'), ('NUH', 'NUH KÖYÜ, İSTİKLAL MEVKİİ'), ('SER', 'SERBAN BELDESİ, CUMHURİYET MAHALLESİ'), ('SER', 'SERBAN BELDESİ, HİSAR MAHALLESİ'), ('SER', 'SERBAN BELDESİ, KÖPRÜBAŞI MAHALLESİ'), ('SER', 'SERBAN BELDESİ, KÜMBET MAHALLESİ'), ('SER', 'SERBAN BELDESİ, ORTA MAHALLESİ'), ('SER', 'SERBAN BELDESİ, HOZMAN MAHALLESİ'), ('TAŞ', 'TAŞOLUK BELDESİ, BAHÇELİEVLER MAHALLESİ'), ('TAŞ', 'TAŞOLUK BELDESİ, CUMHURİYET MAHALLESİ'), ('TAŞ', 'TAŞOLUK BELDESİ, ÇANKAYA MAHALLESİ'), ('TAŞ', 'TAŞOLUK BELDESİ, ÇINARLI MAHALLESİ'), ('TAŞ', 'TAŞOLUK BELDESİ, HÜRRİYET MAHALLESİ'), ('TAŞ', 'TAŞOLUK BELDESİ, YENİ MAHALLESİ'), ('TIN', 'TINAZTEPE BELDESİ, AMBAR MAHALLESİ')], default='adf', max_length=100),
            preserve_default=False,
        ),
    ]