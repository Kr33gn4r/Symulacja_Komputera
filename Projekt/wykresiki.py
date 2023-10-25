import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('tkagg')

df_fifo = pd.read_excel("nowy.xlsx", sheet_name="Fifo", dtype={"queue": str, "number_of_ppl": int, "avg_get_up_speed": int, "avg_walking_speed": float, "time": float})
df_pulse = pd.read_excel("nowy.xlsx", sheet_name="Pulse", dtype={"queue": str, "number_of_ppl": int, "avg_get_up_speed": int, "avg_walking_speed": float, "time": float})
df_bf = pd.read_excel("nowy.xlsx", sheet_name="BestFirst", dtype={"queue": str, "number_of_ppl": int, "avg_get_up_speed": int, "avg_walking_speed": float, "time": float})
df_nr = pd.read_excel("nowy.xlsx", sheet_name="PlaceFirst", dtype={"queue": str, "number_of_ppl": int, "avg_get_up_speed": int, "avg_walking_speed": float, "time": float})

fifo_full = np.average(df_fifo.loc[:, "time"].to_numpy())
fifo_t_50 = np.average(df_fifo.loc[lambda df: df["number_of_ppl"] == 50, "time"].to_numpy())
fifo_t_100 = np.average(df_fifo.loc[lambda df: df["number_of_ppl"] == 100, "time"].to_numpy())
fifo_t_150 = np.average(df_fifo.loc[lambda df: df["number_of_ppl"] == 150, "time"].to_numpy())
fifo_m_1 = np.average(df_fifo.loc[lambda df: df["avg_walking_speed"] == 1, "time"].to_numpy())
fifo_m_2 = np.average(df_fifo.loc[lambda df: df["avg_walking_speed"] == 1.3, "time"].to_numpy())
fifo_m_3 = np.average(df_fifo.loc[lambda df: df["avg_walking_speed"] == 1.6, "time"].to_numpy())
fifobox = df_fifo.loc[:, "time"].to_numpy()

pulse_t_50 = np.average(df_pulse.loc[lambda df: df["number_of_ppl"] == 50, "time"].to_numpy())
pulse_t_100 = np.average(df_pulse.loc[lambda df: df["number_of_ppl"] == 100, "time"].to_numpy())
pulse_full = np.average(df_pulse.loc[:, "time"].to_numpy())
pulse_t_150 = np.average(df_pulse.loc[lambda df: df["number_of_ppl"] == 150, "time"].to_numpy())
pulse_m_1 = np.average(df_pulse.loc[lambda df: df["avg_walking_speed"] == 1, "time"].to_numpy())
pulse_m_2 = np.average(df_pulse.loc[lambda df: df["avg_walking_speed"] == 1.3, "time"].to_numpy())
pulse_m_3 = np.average(df_pulse.loc[lambda df: df["avg_walking_speed"] == 1.6, "time"].to_numpy())
pulsebox = df_pulse.loc[:, "time"].to_numpy()

bf_full = np.average(df_bf.loc[:, "time"].to_numpy())
bf_t_50 = np.average(df_bf.loc[lambda df: df["number_of_ppl"] == 50, "time"].to_numpy())
bf_t_100 = np.average(df_bf.loc[lambda df: df["number_of_ppl"] == 100, "time"].to_numpy())
bf_t_150 = np.average(df_bf.loc[lambda df: df["number_of_ppl"] == 150, "time"].to_numpy())
bf_m_1 = np.average(df_bf.loc[lambda df: df["avg_walking_speed"] == 1, "time"].to_numpy())
bf_m_2 = np.average(df_bf.loc[lambda df: df["avg_walking_speed"] == 1.3, "time"].to_numpy())
bf_m_3 = np.average(df_bf.loc[lambda df: df["avg_walking_speed"] == 1.6, "time"].to_numpy())
bfbox = df_bf.loc[:, "time"].to_numpy()

nr_full = np.average(df_nr.loc[:, "time"].to_numpy())
nr_t_50 = np.average(df_nr.loc[lambda df: df["number_of_ppl"] == 50, "time"].to_numpy())
nr_t_100 = np.average(df_nr.loc[lambda df: df["number_of_ppl"] == 100, "time"].to_numpy())
nr_t_150 = np.average(df_nr.loc[lambda df: df["number_of_ppl"] == 150, "time"].to_numpy())
nr_m_1 = np.average(df_nr.loc[lambda df: df["avg_walking_speed"] == 1, "time"].to_numpy())
nr_m_2 = np.average(df_nr.loc[lambda df: df["avg_walking_speed"] == 1.3, "time"].to_numpy())
nr_m_3 = np.average(df_nr.loc[lambda df: df["avg_walking_speed"] == 1.6, "time"].to_numpy())
nrbox = df_nr.loc[:, "time"].to_numpy()

fifo_t = [fifo_t_50, fifo_t_100, fifo_t_150]
pulse_t = [pulse_t_50, pulse_t_100, pulse_t_150]
bf_t = [bf_t_50, bf_t_100, bf_t_150]
nr_t = [nr_t_50, nr_t_100, nr_t_150]

fifo_m = [fifo_m_1, fifo_m_2, fifo_m_3]
pulse_m = [pulse_m_1, pulse_m_2, pulse_m_3]
bf_m = [bf_m_1, bf_m_2, bf_m_3]
nr_m = [nr_m_1, nr_m_2, nr_m_3]

all_methods = [fifo_full, pulse_full, bf_full, nr_full]

plt.style.use('ggplot')
plt.rcParams["figure.figsize"] = (1920/96, 1080/96)

f, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, sharey=True)
ax1.plot([50, 100, 150], fifo_t, color="tab:red", label="FIFO")
ax1.plot([50, 100, 150], pulse_t, color="tab:green", label="Pulse")
ax1.plot([50, 100, 150], bf_t, color="tab:blue", label="BestFirst")
ax1.plot([50, 100, 150], nr_t, color="black", label="PlaceFirst")
ax1.legend()
ax1.set_xlabel("Ilość osób")
ax1.set_ylabel("Czas")
ax1.set_title("Wykres zależności czasu od ilości osób\ndla wszystkich algorytmów kolejki")
ax1.set_xticks([50, 100, 150])

ax2.plot([1.0, 1.3, 1.6], fifo_m, color="tab:red", label="FIFO")
ax2.plot([1.0, 1.3, 1.6], pulse_m, color="tab:green", label="Pulse")
ax2.plot([1.0, 1.3, 1.6], bf_m, color="tab:blue", label="BestFirst")
ax2.plot([1.0, 1.3, 1.6], nr_m, color="black", label="PlaceFirst")
ax2.legend()
ax2.set_xlabel("Średnia prędkość chodzenia")
ax2.set_ylabel("Czas")
ax2.set_title("Wykres zależności czasu od średniej prędkości chodzenia\ndla wszystkich algorytmów kolejki")
ax2.set_xticks([1.0, 1.3, 1.6])

"""
ax3.bar(["FIFO", "Pulse", "BestFirst", "PlaceFirst"], all_methods)
ax3.get_children()[0].set_color('tab:red')
ax3.get_children()[1].set_color('tab:green')
ax3.get_children()[2].set_color('tab:blue')
ax3.get_children()[3].set_color('black')
ax3.set_xlabel("Algorytm kolejki")
ax3.set_ylabel("Czas")
ax3.set_title("Wykres średniego czasu działania algorytmu")
"""

boxplotarray = [fifobox, pulsebox, bfbox, nrbox]
ax3.boxplot(boxplotarray, 0, '', labels=["FIFO", "Pulse", "Best First", "Number First"])
ax3.set_xlabel("Algorytm kolejki")
ax3.set_ylabel("Czas")
ax3.set_title("Wykres pudełkowy czasu działania algorytmu")

plt.savefig("wykresy.png", dpi=96)
plt.show()