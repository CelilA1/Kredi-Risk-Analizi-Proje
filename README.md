# Kredi Risk Analizi - Python Proje

Bu proje, kredi başvurularının risk durumlarını makine öğrenmesi algoritmalarıyla analiz ederek, başvurunun onaylanıp onaylanmaması gerektiğini tahmin etmeyi amaçlamaktadır. Model, kullanıcıdan alınan finansal ve demografik veriler doğrultusunda kredi risk tahmini yapar ve güven skoru ile birlikte sonuçları sunar.

## 📌 Proje Amacı

- Kredi risklerini yüksek doğrulukla tahmin etmek
- Farklı sınıflandırma algoritmalarını karşılaştırmak
- En iyi modeli belirleyip optimize etmek
- Kullanıcı dostu bir arayüz tasarlamak
- Görsel grafiklerle sonuçları anlaşılır kılmak

## ⚙️ Kullanılan Teknolojiler

- **Programlama Dili:** Python 3.13  
- **Kütüphaneler:** 
  - Veri Analizi: `Pandas`, `NumPy`
  - Makine Öğrenimi: `Scikit-learn`, `XGBoost`
  - Görselleştirme: `Matplotlib`, `Seaborn`
  - Arayüz: `QtCreator (PySide6)`
  - Model Kaydetme: `Joblib`

## 🧠 Kullanılan Modeller

- Logistic Regression
- Random Forest
- **XGBoost** (En iyi performans gösterdiği için tercih edildi)

## 🔍 Veri Seti Özellikleri

- Yaş, gelir, ev sahipliği, kredi amacı, kredi notu, faiz oranı, kredi miktarı gibi bireysel ve finansal bilgiler içerir.
- Eksik ve aykırı veriler temizlenmiştir.
- Kategorik veriler sayısallaştırılmış, sayısal veriler ölçeklendirilmiştir.
- Veri dengesizliği SMOTE ile dengelenmiştir.

## 🖥️ Arayüz Özellikleri

- Kullanıcıdan 11 veri alarak kredi riski hesaplaması yapar.
- Tahmin sonucu ve güven skoru gösterilir.
- Veri setine ait görselleştirme seçenekleri sunulur.

## 📊 Görselleştirmeler

- Veri dağılımları ve değişken ilişkileri grafiklerle sunulmuştur.
- Arayüz üzerinden kullanıcı, seçtiği grafikleri görüntüleyebilir.

## 📁 Veri Seti

Kullanılan veri setine [buradan](https://www.kaggle.com/datasets/laotse/credit-risk-dataset) ulaşabilirsiniz.

## 👥 Geliştiriciler

- Muhammed Celil Ayhan  
- Ali Kağan Şeren  
- Berat Çam  
- İsmail Karatay
