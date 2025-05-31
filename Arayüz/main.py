import sys
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QMessageBox
from interface import *
import pandas as pd
import joblib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from pathlib import Path

base_path = Path(__file__).parent

project_root = base_path.parent

csv_path = project_root / "ModelAnaliz" / "credit_risk_dataset.csv"

df = pd.read_csv(csv_path)

df = df.dropna()

df['loan_status'] = df['loan_status'].map({1: 'Approved', 0: 'Rejected'})

class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure(figsize=(6, 5), dpi=100)
        self.ax = self.fig.add_subplot(111) 
        super().__init__(self.fig)

class ChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grafik ve Tablo Penceresi")
        self.setFixedSize(350, 200)

        self.df = df
        self.combo = QComboBox()
        self.combo.addItems([
            "E0",
            "Kredi Türüne Göre Başvuru Dağılımı",
            "Kredi Türüne Göre Ortalama Faiz Oranı (%)",
            "Kredi Notuna Göre Onay Durumu",
            "Kredi Geçmişi Süresi Dağılımı",
            "Kredi Notuna Göre Ortalama Kredi Tutarı",
            "Kredi Türüne Göre Ortalama Gelir",
            "Ev Sahipliği Durumuna Göre Başvuru Sayısı",
            "Çalışma Süresine Göre Ortalama Kredi Tutarı",
            "Başvuru Yapanların Yaş Dağılımı",
            "Kredi Türüne Göre Başvuranların Medyan Yaşı",
            "Onay Durumuna Göre Kredi Tutarı Dağılımı",
            "Kredi Notuna Göre Kredi Tutarı",
            "Kredi Türüne Göre Ortalama Kredi Tutarı",
            "Kredi Türüne Göre Faiz Oranı Dağılımı",
            "Kredi Tutarı, Faiz, Gelir ve Kredi Geçmişi Korelasyonu",
            "Kredi Onay Durumu Dağılımı",
            "Kredi Amaçlarına Göre Dağılım",
            "Kredi Tutarı Dağılımı",
            "Faiz Oranı Dağılımı",
            "Gelir ve Kredi Tutarı",
            "Kredi Geçmişi Süresi, Faiz Oranı ve Kredi Tutarı",
            "Kredi Amacına Göre Faiz Oranı Dağılımı",
            "Önemli Değişkenlerin Korelasyon Matrisi",
            "Ev Sahipliği ve Kredi Onay Durumu",
            "Kredi Notuna Göre Gelir Dağılımı",
            "3D Scatter: Yaş, Gelir ve Kredi Tutarı",
            "Kredi Notlarına Göre Ortalama Değerler",
            "Yaş Aralığına Göre Kredi Onay Oranı (%)",
            "Gelir Aralığına Göre Kredi Tutarı Dağılımı"
        ])

        self.combo.currentTextChanged.connect(self.plot_graph)

        self.combo.setStyleSheet("""
            QComboBox {
                font-size: 16px;
                padding: 5px 15px;
                border: 2px solid #0078d7;
                border-radius: 8px;
                min-width: 140px;
            }
        """)

        self.canvas = MplCanvas()

        self.combo.setToolTip("Grafik türünü buradan seçebilirsiniz")

        container = QWidget()
        v_layout = QVBoxLayout()

        label = QLabel("Lütfen Grafik Türünü Seçiniz")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-weight: bold; font-size: 18px; margin-bottom: 15px;")
        v_layout.addStretch()
        v_layout.addWidget(label)
        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(self.combo)
        h_layout.addStretch()
        v_layout.addLayout(h_layout)
        v_layout.addStretch()

        container.setLayout(v_layout)
        self.setCentralWidget(container)

        self.plot_graph(self.combo.currentText())

    def plot_graph(self, graph_type):
        self.canvas.fig.clf()
        self.canvas.ax = self.canvas.fig.add_subplot(111)

        if graph_type == "E0":
            pass

        elif graph_type == "Kredi Türüne Göre Başvuru Dağılımı":
            plt.figure(figsize=(8, 5))
            sns.set_theme(style="whitegrid")
            sns.set_palette("Set2")
    
            ax = sns.countplot(data=df, x='loan_intent', order=df['loan_intent'].value_counts().index)
            plt.title("Kredi Türüne Göre Başvuru Dağılımı")
            plt.xlabel("Kredi Türü")
            plt.ylabel("Başvuru Sayısı")
            plt.xticks(rotation=45)

            for p in ax.patches:
                ax.annotate(f'{p.get_height()}', 
                            (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='bottom')

            plt.tight_layout()
            plt.show()

        elif graph_type == "Kredi Türüne Göre Ortalama Faiz Oranı (%)":
            plt.figure(figsize=(8, 5))
            sns.set_theme(style="whitegrid")
            sns.set_palette("pastel")

            ax = sns.barplot(data=df, x='loan_intent', y='loan_int_rate', estimator='mean')
            plt.title("Kredi Türüne Göre Ortalama Faiz Oranı (%)")
            plt.xlabel("Kredi Türü")
            plt.ylabel("Ortalama Faiz (%)")
            plt.xticks(rotation=45)

            for p in ax.patches:
                height = p.get_height()
                if not np.isnan(height):
                    ax.annotate(f'{height:.2f}', (p.get_x() + p.get_width() / 2., height),
                                ha='center', va='bottom')

            plt.tight_layout()
            plt.show()

        elif graph_type == "Kredi Notuna Göre Onay Durumu":
            plt.figure(figsize=(8, 5))
            sns.set_theme(style="whitegrid")
            ax = sns.countplot(data=df, x='loan_grade', hue='loan_status', order=sorted(df['loan_grade'].unique()), palette="Set1")

            plt.title("Kredi Notuna Göre Onay Durumu")
            plt.xlabel("Kredi Notu (Grade)")
            plt.ylabel("Başvuru Sayısı")
            plt.legend(title="Durum")

            for p in ax.patches:
                height = p.get_height()
                if height > 0:
                    ax.annotate(f'{height}', (p.get_x() + p.get_width() / 2., height),
                                ha='center', va='bottom', fontsize=8)

            plt.tight_layout()
            plt.show()

        elif graph_type == "Kredi Geçmişi Süresi Dağılımı":
            plt.figure(figsize=(8, 5))
            sns.set_theme(style="whitegrid")
            ax = sns.histplot(df['cb_person_cred_hist_length'], bins=15, kde=True, color="skyblue")

            plt.title("Kredi Geçmişi Süresi Dağılımı")
            plt.xlabel("Yıl")
            plt.ylabel("Kişi Sayısı")

            for p in ax.patches:
                height = p.get_height()
                if height > 0:
                    ax.annotate(f'{int(height)}', (p.get_x() + p.get_width() / 2., height),
                                ha='center', va='bottom', fontsize=8)

            plt.tight_layout()
            plt.show()

        elif graph_type == "Kredi Notuna Göre Ortalama Kredi Tutarı":
            plt.figure(figsize=(8, 5))
            sns.set_theme(style="whitegrid")
            ax = sns.barplot(data=df, x='loan_grade', y='loan_amnt', estimator='mean', palette='coolwarm')

            plt.title("Kredi Notuna Göre Ortalama Kredi Tutarı")
            plt.xlabel("Kredi Notu")
            plt.ylabel("Ortalama Tutar")

            for p in ax.patches:
                height = p.get_height()
                ax.annotate(f'{height:.0f}', (p.get_x() + p.get_width() / 2., height), ha='center', va='bottom', fontsize=8)

            plt.tight_layout()
            plt.show()

        elif graph_type == "Kredi Türüne Göre Ortalama Gelir":
            plt.figure(figsize=(8, 5))
            sns.set_theme(style="whitegrid")
            ax = sns.barplot(data=df, x='loan_intent', y='person_income', estimator='mean', palette='YlOrBr')

            plt.title("Kredi Türüne Göre Ortalama Gelir")
            plt.xlabel("Kredi Türü")
            plt.ylabel("Ortalama Gelir")
            plt.xticks(rotation=45)

            for p in ax.patches:
                height = p.get_height()
                ax.annotate(f'{height:.0f}', (p.get_x() + p.get_width() / 2., height), ha='center', va='bottom', fontsize=8)

            plt.tight_layout()
            plt.show()

        elif graph_type == "Ev Sahipliği Durumuna Göre Başvuru Sayısı":
            plt.figure(figsize=(8, 5))
            sns.set_theme(style="whitegrid")
            ax = sns.countplot(data=df, x='person_home_ownership', palette="Set3", order=df['person_home_ownership'].value_counts().index)
    
            plt.title("Ev Sahipliği Durumuna Göre Başvuru Sayısı")
            plt.xlabel("Ev Sahipliği Durumu")
            plt.ylabel("Başvuru Sayısı")

            for p in ax.patches:
                height = p.get_height()
                ax.annotate(f'{height}', (p.get_x() + p.get_width() / 2., height), ha='center', va='bottom', fontsize=8)

            plt.tight_layout()
            plt.show()

        elif graph_type == "Çalışma Süresine Göre Ortalama Kredi Tutarı":
            max_emp_length = 60
            df_filtered = df[df['person_emp_length'] <= max_emp_length]

            plt.figure(figsize=(8, 5))
            sns.set_theme(style="whitegrid")
            ax = sns.barplot(data=df_filtered, x='person_emp_length', y='loan_amnt', 
                             estimator='mean', palette="coolwarm", ci=None)

            plt.title("Çalışma Süresine Göre Ortalama Kredi Tutarı")
            plt.xlabel("Çalışma Süresi (Yıl)")
            plt.ylabel("Ortalama Kredi Tutarı")

            for p in ax.patches:
                height = p.get_height()
                if height is not None:
                    ax.annotate(f'{height:.0f}', 
                                (p.get_x() + p.get_width() / 2., height), 
                                ha='center', va='bottom', fontsize=8)

            plt.tight_layout()
            plt.show()

        elif graph_type == "Başvuru Yapanların Yaş Dağılımı":
            max_age = 90
            df_filtered = df[df['person_age'] <= max_age]

            plt.figure(figsize=(8, 5))
            sns.set_theme(style="whitegrid")
            ax = sns.histplot(data=df_filtered, x='person_age', bins=20, kde=True, color="orange")

            plt.title("Başvuru Yapanların Yaş Dağılımı")
            plt.xlabel("Yaş")
            plt.ylabel("Başvuru Sayısı")

            for p in ax.patches:
                height = p.get_height()
                if height > 0:
                    ax.annotate(f'{int(height)}', 
                                (p.get_x() + p.get_width() / 2., height), 
                                ha='center', va='bottom', fontsize=8)

            plt.tight_layout()
            plt.show()

        elif graph_type == "Kredi Türüne Göre Başvuranların Medyan Yaşı":
            plt.figure(figsize=(8, 5))
            sns.set_theme(style="whitegrid")
            ax = sns.barplot(data=df, x='loan_intent', y='person_age', estimator='median', palette='magma')

            plt.title("Kredi Türüne Göre Başvuranların Medyan Yaşı")
            plt.xlabel("Kredi Türü")
            plt.ylabel("Medyan Yaş")
            plt.xticks(rotation=45)

            for p in ax.patches:
                height = p.get_height()
                ax.annotate(f'{height:.0f}', (p.get_x() + p.get_width() / 2., height), ha='center', va='bottom', fontsize=8)

            plt.tight_layout()
            plt.show()

        elif graph_type == "Onay Durumuna Göre Kredi Tutarı Dağılımı":
            plt.figure(figsize=(8, 5))
            sns.set_theme(style="darkgrid")
            ax = sns.violinplot(data=df, x='loan_status', y='loan_amnt', palette="muted")
    
            plt.title("Onay Durumuna Göre Kredi Tutarı Dağılımı (Violin Plot)")
            plt.xlabel("Onay Durumu")
            plt.ylabel("Kredi Tutarı")
    
            plt.tight_layout()
            plt.show()

        elif graph_type == "Kredi Notuna Göre Kredi Tutarı":
            plt.figure(figsize=(8, 5))
            sns.set_theme(style="ticks")
            sns.stripplot(data=df, x='loan_grade', y='loan_amnt', hue='loan_status', jitter=True, dodge=True, palette="Set2")
    
            plt.title("Kredi Notuna Göre Kredi Tutarı (Strip Plot)")
            plt.xlabel("Kredi Notu")
            plt.ylabel("Kredi Tutarı")
            plt.legend(title="Onay Durumu", bbox_to_anchor=(1.05, 1), loc='upper left')
    
            plt.tight_layout()
            plt.show()

        elif graph_type == "Kredi Türüne Göre Ortalama Kredi Tutarı":
            plt.figure(figsize=(8, 5))
            sns.set_theme(style="darkgrid")
            ax = sns.lineplot(data=df.groupby('loan_intent')['loan_amnt'].mean().reset_index(),
                              x='loan_intent', y='loan_amnt', marker="o", sort=False)
            plt.title("Kredi Türüne Göre Ortalama Kredi Tutarı (Line Plot)")
            plt.xlabel("Kredi Türü")
            plt.ylabel("Ortalama Kredi Tutarı")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        elif graph_type == "Kredi Türüne Göre Faiz Oranı Dağılımı":
            plt.figure(figsize=(8, 5))
            sns.set_theme(style="whitegrid")
            sns.violinplot(data=df, x='loan_intent', y='loan_int_rate', palette="Pastel1")
            plt.title("Kredi Türüne Göre Faiz Oranı Dağılımı (Violin Plot)")
            plt.xlabel("Kredi Türü")
            plt.ylabel("Faiz Oranı (%)")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        elif graph_type == "Kredi Tutarı, Faiz, Gelir ve Kredi Geçmişi Korelasyonu":
            plt.figure(figsize=(8, 5))
            sns.set_theme(style="white")
            corr = df[['loan_amnt', 'loan_int_rate', 'person_income', 'cb_person_cred_hist_length']].corr()
            sns.heatmap(corr, annot=True, cmap="YlGnBu", fmt=".2f")
            plt.title("Kredi Tutarı, Faiz, Gelir ve Kredi Geçmişi Korelasyonu")
            plt.tight_layout()
            plt.show()

        elif graph_type == "Kredi Onay Durumu Dağılımı":
            plt.figure(figsize=(6,6))
            counts = df['loan_status'].value_counts()
            plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Set2"))
            plt.title("Kredi Onay Durumu Dağılımı (Pie Chart)")
            plt.show()

        elif graph_type == "Kredi Amaçlarına Göre Dağılım":
            plt.figure(figsize=(7,7))
            counts = df['loan_intent'].value_counts()
            explode = [0.1 if i == counts.idxmax() else 0 for i in counts.index]
            plt.pie(counts, labels=counts.index, autopct='%1.1f%%', explode=explode, startangle=60, colors=sns.color_palette("tab20"))
            plt.title("Kredi Amaçlarına Göre Dağılım (Vurgulu Dilim)")
            plt.show()

        elif graph_type == "Kredi Tutarı Dağılımı":
            plt.figure(figsize=(8,5))
            sns.histplot(df['loan_amnt'], bins=30, kde=False, color="cornflowerblue")
            plt.title("Kredi Tutarı Dağılımı (Histogram)")
            plt.xlabel("Kredi Tutarı")
            plt.ylabel("Frekans")
            plt.tight_layout()
            plt.show()

        elif graph_type == "Faiz Oranı Dağılımı":
            plt.figure(figsize=(8,5))
            sns.histplot(df, x='loan_int_rate', bins=25, kde=True, color="seagreen")
            plt.title("Faiz Oranı Dağılımı (KDE Histogram)")
            plt.xlabel("Faiz Oranı (%)")
            plt.ylabel("Frekans")
            plt.tight_layout()
            plt.show()

        elif graph_type == "Gelir ve Kredi Tutarı":
            max_income = 500000
            df_filtered = df[df['person_income'] <= max_income]
    
            if len(df_filtered) > 10000:
                df_sample = df_filtered.sample(10000, random_state=42)
            else:
                df_sample = df_filtered
    
            plt.figure(figsize=(8,5))
            sns.scatterplot(data=df_sample, x='person_income', y='loan_amnt', 
                            hue='loan_status', style='person_home_ownership', 
                            palette='Set2', alpha=0.7)
            plt.title("Gelir ve Kredi Tutarı (Scatter Plot)")
            plt.xlabel("Kişisel Gelir")
            plt.ylabel("Kredi Tutarı")
            plt.legend(title="Onay Durumu & Ev Sahipliği", bbox_to_anchor=(1.05,1))
            plt.tight_layout()
            plt.show()

        elif graph_type == "Kredi Geçmişi Süresi, Faiz Oranı ve Kredi Tutarı":
            plt.figure(figsize=(8,5))
            sns.scatterplot(data=df, x='cb_person_cred_hist_length', y='loan_int_rate', size='loan_amnt', sizes=(20, 200), hue='loan_status', alpha=0.6, palette="cool")
            plt.title("Kredi Geçmişi Süresi, Faiz Oranı ve Kredi Tutarı (Bubble Plot)")
            plt.xlabel("Kredi Geçmişi Süresi (Yıl)")
            plt.ylabel("Faiz Oranı (%)")
            plt.legend(title="Onay Durumu", bbox_to_anchor=(1.05,1))
            plt.tight_layout()
            plt.show()

        elif graph_type == "Kredi Amacına Göre Faiz Oranı Dağılımı":
            plt.figure(figsize=(8,5))
            sns.violinplot(data=df, x='loan_intent', y='loan_int_rate', palette="pastel")
            plt.title("Kredi Amacına Göre Faiz Oranı Dağılımı (Violin Plot)")
            plt.xlabel("Kredi Amacı")
            plt.ylabel("Faiz Oranı (%)")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        elif graph_type == "Önemli Değişkenlerin Korelasyon Matrisi":
            plt.figure(figsize=(8,6))
            corr = df[['loan_amnt', 'loan_int_rate', 'person_income', 'cb_person_cred_hist_length', 'person_emp_length']].corr()
            sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
            plt.title("Önemli Değişkenlerin Korelasyon Matrisi")
            plt.tight_layout()
            plt.show()

        elif graph_type == "Ev Sahipliği ve Kredi Onay Durumu":
            status_counts = df.groupby(['person_home_ownership', 'loan_status']).size().unstack()
            status_counts.plot(kind='bar', stacked=True, figsize=(10,6), colormap='tab20')
            plt.title("Ev Sahipliği ve Kredi Onay Durumu")
            plt.xlabel("Ev Sahipliği")
            plt.ylabel("Başvuru Sayısı")
            plt.xticks(rotation=45)
            plt.show()

        elif graph_type == "Kredi Notuna Göre Gelir Dağılımı":
            max_income = 300000
            df_filtered = df[df['person_income'] <= max_income]
    
            plt.figure(figsize=(10,6))
            sns.boxenplot(x='loan_grade', y='person_income', data=df_filtered, palette='coolwarm')
            plt.title("Kredi Notuna Göre Gelir Dağılımı")
            plt.show()

        elif graph_type == "3D Scatter: Yaş, Gelir ve Kredi Tutarı":
            max_age = 80
            max_income = 200000
    
            df_filtered = df[(df['person_age'] <= max_age) & (df['person_income'] <= max_income)]
    
            fig = plt.figure(figsize=(14, 10))
            ax = fig.add_subplot(111, projection='3d')
    
            scatter = ax.scatter(
                df_filtered['person_age'], 
                df_filtered['person_income'], 
                df_filtered['loan_amnt'],
                c=df_filtered['loan_int_rate'], 
                cmap='viridis', 
                alpha=0.3,
                edgecolor='none',
                s=10
            )
    
            ax.set_xlabel('Yaş', fontsize=14, labelpad=15)
            ax.set_ylabel('Gelir', fontsize=14, labelpad=15)
            ax.set_zlabel('Kredi Tutarı', fontsize=14, labelpad=15)
    
            plt.title(f"3D Scatter: Yaş, Gelir ve Kredi Tutarı")
    
            cbar = plt.colorbar(scatter, pad=0.1)
            cbar.set_label('Faiz Oranı', fontsize=14)
    
            ax.view_init(elev=25, azim=140)
    
            plt.tight_layout()
            plt.show()

        elif graph_type == "Kredi Notlarına Göre Ortalama Değerler":
            categories = ['person_age', 'person_income', 'loan_amnt', 'loan_int_rate', 'person_emp_length']
    
            group_means = df.groupby('loan_grade')[categories].mean()
    
            scaler = MinMaxScaler()
            normalized_values = scaler.fit_transform(group_means)
            normalized_df = pd.DataFrame(normalized_values, columns=categories, index=group_means.index)
    
            labels = categories
            num_vars = len(labels)
    
            angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
            angles += angles[:1]
    
            fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
    
            for grade in normalized_df.index:
                values = normalized_df.loc[grade].tolist()
                values += values[:1]
        
                ax.plot(angles, values, label=f'Not: {grade}', linewidth=2)
                ax.fill(angles, values, alpha=0.25)
    
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(labels, fontsize=12)
    
            ax.set_yticklabels([])
    
            plt.title("Kredi Notlarına Göre Ortalama Değerler (Normalize Edilmiş Radar Grafiği)", fontsize=14, fontweight='bold', pad=20)
            plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1.1))
            plt.tight_layout()
            plt.show()

        elif graph_type == "Yaş Aralığına Göre Kredi Onay Oranı (%)":
            df['age_group'] = pd.cut(df['person_age'], bins=[18,25,35,45,55,65,100],
                                     labels=["18-25", "26-35", "36-45", "46-55", "56-65", "65+"])
            age_approval = df[df['loan_status'] == 'Approved']['age_group'].value_counts()
            age_total = df['age_group'].value_counts()
            approval_rate = (age_approval / age_total * 100).sort_index()

            plt.figure(figsize=(10,6))
            ax = sns.barplot(x=approval_rate.index, y=approval_rate.values, palette="ch:s=.25,rot=-.25")
            plt.title("Yaş Aralığına Göre Kredi Onay Oranı (%)")
            plt.ylabel("Onay Oranı (%)")
            plt.xlabel("Yaş Grubu")

            for i, v in enumerate(approval_rate.values):
                ax.text(i, v + 1, f"{v:.1f}%", ha='center', fontsize=11, color='black')

            plt.ylim(0, max(approval_rate.values)*1.15)
            plt.show()

        elif graph_type == "Gelir Aralığına Göre Kredi Tutarı Dağılımı":
            df['income_group'] = pd.cut(df['person_income'], bins=[0,25000,50000,75000,100000,200000,500000],
                                        labels=["0-25K","25-50K","50-75K","75-100K","100-200K","200K+"])
            plt.figure(figsize=(10,6))
            sns.boxplot(x='income_group', y='loan_amnt', data=df, palette="Set2")
            plt.title("Gelir Aralığına Göre Kredi Tutarı Dağılımı")
            plt.ylabel("Kredi Miktarı")
            plt.xlabel("Gelir Grubu")
            plt.xticks(rotation=45)
            plt.show()

        self.canvas.draw()


base_path = Path(__file__).parent
project_root = base_path.parent

csv_path = project_root / "ModelAnaliz" / "credit_risk_dataset.csv"
df = pd.read_csv(csv_path)
df = df.dropna()
df['loan_status'] = df['loan_status'].map({1: 'Approved', 0: 'Rejected'})


model_path = project_root / "ModelAnaliz" / "best_model.pkl"
scaler_path = project_root / "ModelAnaliz" / "scaler.pkl"
feature_columns_path = project_root / "ModelAnaliz" / "feature_columns.pkl"

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)
loaded_feature_columns_list = joblib.load(feature_columns_path)
feature_columns = pd.Index(loaded_feature_columns_list)
print("Özellik sütunları başarıyla yüklendi.")# ---------------------------------------------

print("Modelin beklediği tüm özellik sütunları (feature_columns):")
print(feature_columns.tolist())
model = None
scaler = None
feature_columns = pd.Index([])

try:
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    loaded_feature_columns_list = joblib.load(feature_columns_path)

    desired_ohe_features = [
        'person_home_ownership_OTHER',
        'person_home_ownership_OWN',
        'person_home_ownership_RENT',
        'loan_intent_EDUCATION',
        'loan_intent_HOMEIMPROVEMENT',
        'loan_intent_MEDICAL',
        'loan_intent_PERSONAL',
        'loan_intent_VENTURE',
        'cb_person_default_on_file_Y'
    ]

    non_ohe_features_to_keep = [
        'person_age',
        'person_income',
        'person_emp_length',
        'loan_grade',
        'loan_amnt',
        'loan_int_rate',
        'loan_percent_income',
        'cb_person_cred_hist_length'
    ]

    final_feature_columns_list = [
        col for col in loaded_feature_columns_list
        if col in (set(non_ohe_features_to_keep) | set(desired_ohe_features))
    ]

    feature_columns = pd.Index(final_feature_columns_list)
    print("Model, Scaler ve Özellik Sütunları başarıyla yüklendi ve filtrelendi.")
    print("Güncellenmiş feature_columns:", feature_columns.tolist())

except FileNotFoundError as e:
    QMessageBox.critical(None, "Yükleme Hatası", f"Gerekli model/scaler/özellik dosyaları bulunamadı:\n{e}\n"
                                                 f"Lütfen 'ModelAnaliz' klasöründeki dosyaların doğru olduğundan emin olun.")
    sys.exit(1)
except Exception as e:
    QMessageBox.critical(None, "Yükleme Hatası",
                         f"Model/scaler/özellik dosyaları yüklenirken beklenmeyen bir hata oluştu:\n{e}")
    sys.exit(1)

categorical_cols_for_dummies = ['person_home_ownership', 'loan_intent',
                                'cb_person_default_on_file']

grade_mapping = {
    "G": 0, "F": 1, "E": 2, "D": 3, "C": 4, "B": 5, "A": 6
}
normalization_columns = ["person_income", "person_age", "loan_amnt", "loan_int_rate", "person_emp_length"]


def preprocess_single_data(single_dict):

    df_single = pd.DataFrame([single_dict])

    if 'cb_person_default_on_file' in df_single.columns:
        if df_single['cb_person_default_on_file'].iloc[0] == 'YES':
            df_single['cb_person_default_on_file'] = 'Y'
        elif df_single['cb_person_default_on_file'].iloc[0] == 'NO':
            df_single['cb_person_default_on_file'] = 'N'

    df_single['loan_grade'] = df_single['loan_grade'].map(grade_mapping)

    ohe_columns_in_features = [col for col in feature_columns if
                               any(col.startswith(cat_col + '_') for cat_col in categorical_cols_for_dummies)]

    ohe_template_df = pd.DataFrame(0, index=[0], columns=ohe_columns_in_features)

    temp_categorical_data = {}
    for col in categorical_cols_for_dummies:
        if col in df_single.columns:
            temp_categorical_data[col] = df_single[col].iloc[0]

    df_single = df_single.drop(columns=categorical_cols_for_dummies, errors='ignore')

    for original_col, selected_value in temp_categorical_data.items():
        ohe_col_name = f"{original_col}_{selected_value}"
        if ohe_col_name in ohe_template_df.columns:
            ohe_template_df[ohe_col_name] = 1

    df_single = pd.concat([df_single, ohe_template_df], axis=1)

    missing_cols_final = feature_columns.difference(df_single.columns)
    for col in missing_cols_final:
        df_single[col] = 0

    extra_cols_final = df_single.columns.difference(feature_columns)
    if not extra_cols_final.empty:
        df_single = df_single.drop(columns=extra_cols_final)

    df_single = df_single[feature_columns]

    df_single[normalization_columns] = scaler.transform(df_single[normalization_columns])

    X_processed = df_single.values

    print("\n--- preprocess_single_data Sonuç (DataFrame Hali) ---")
    for col in feature_columns:
        print(f"{col}: {df_single[col].iloc[0]}")

    return X_processed

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.chart_window = None

        self.init_functions()

    def init_functions(self):
        self.ui.pushButton_chart.clicked.connect(self.show_chart_window)
        self.ui.pushButton_chart_3.clicked.connect(self.collect_input_data)

    def collect_input_data(self):
            try:
                person_age = int(self.ui.lineEdit_age.text())
                person_income = int(self.ui.lineEdit_person_income.text())
                person_home_ownership = self.ui.comboBox_person_home_ownership.currentText().strip().upper()
                person_emp_length = float(self.ui.comboBox_person_emp_length.currentText())
                loan_intent = self.ui.comboBox_loan_intent.currentText().strip().upper()
                loan_grade = self.ui.comboBox_loan_grade.currentText().strip().upper()
                loan_amnt = int(self.ui.lineEdit_loan_amnt.text())
                loan_int_rate = float(self.ui.lineEdit_loan_int_rate.text())
                loan_percent_income = float(self.ui.lineEdit_loan_percent_income.text())
                cb_person_default_on_file = self.ui.comboBox_cb_person_default_on_file.currentText().strip().upper()
                cb_person_cred_hist_length = int(self.ui.comboBox_cb_person_cred_hist_length.currentText())

                if person_age <= 0 or person_income < 0 or person_emp_length < 0 or loan_amnt < 0 or loan_int_rate < 0 or loan_percent_income < 0 or cb_person_cred_hist_length < 0:
                    raise ValueError("Değerler pozitif olmalı")

                input_data = {
                    'person_age': person_age,
                    'person_income': person_income,
                    'person_home_ownership': person_home_ownership,
                    'person_emp_length': person_emp_length,
                    'loan_intent': loan_intent,
                    'loan_grade': loan_grade,
                    'loan_amnt': loan_amnt,
                    'loan_int_rate': loan_int_rate,
                    'loan_percent_income': loan_percent_income,
                    'cb_person_default_on_file': cb_person_default_on_file,
                    'cb_person_cred_hist_length': cb_person_cred_hist_length
                }

                X_single = preprocess_single_data(input_data)

                pred = model.predict(X_single)
                proba = model.predict_proba(X_single)

                self.ui.lineEdit_8.setText(str(pred[0]))
                self.ui.lineEdit_9.setText(f"%{round(proba[0][1]*100, 2)}")

            except ValueError as e:
                QMessageBox.warning(self, "Hata", f"Lütfen geçerli değerler girin.\nDetay: {e}")


    def show_chart_window(self):
        if self.chart_window is None:
            self.chart_window = ChartWindow()
            self.chart_window.setAttribute(Qt.WA_DeleteOnClose)
            self.chart_window.destroyed.connect(self.on_chart_closed)

        if self.chart_window is not None:
            self.chart_window.raise_()
            self.chart_window.activateWindow()
            self.chart_window.show()

    def on_chart_closed(self):
        self.chart_window = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())