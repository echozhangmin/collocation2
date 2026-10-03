"""《明史》目标词「内阁」的搭配词分析。

作用：对同一个分词语料，用三种不同的「上下文范围」各跑一次
qhchina 的 find_collocates，把结果分别存成一个 CSV：
  - window5   ：每个「内阁」左右各 5 个词算作它的上下文
  - window10  ：左右各 10 个词
  - sentence  ：整句都算上下文
这样可以看到「上下文放宽后，搭配词怎么变」。

运行方式（在仓库根目录）：  python code/collocations.py
"""
import os

# find_collocates：核心函数，负责数共现、做 Fisher 检验、算关联度量
# load_stopwords ：加载停用词表（这里用文言·简体）
from qhchina import find_collocates, load_stopwords

# SegmentedCorpus 是第一步 prepare.py 产出的分词语料，
# 它可以在被遍历两次（find_collocates 需要扫两遍）
from corpus import SegmentedCorpus

# ── 配置区：以后换关键词/参数基本只改这里 ──────────────────────────

TARGET = "内阁"          # 目标词（想研究谁/什么就改这里，如 "张居正"、"司礼监"）
OUTDIR = "output"        # 结果 CSV 的输出目录

# 三种「上下文范围」设置，各跑一次。名字(name)用作文件名，
# options 会作为关键字参数传给 find_collocates。
RUNS = [
    ("window5",  dict(method="window", horizon=5)),    # 窗口=左右各5词
    ("window10", dict(method="window", horizon=10)),   # 窗口=左右各10词
    ("sentence", dict(method="sentence")),             # 整句为上下文
]

# 筛选条件：只有满足这些条件的搭配词才会保留在结果里
FILTERS = dict(
    # 停用词：去掉「之/乎/者/也/曰……」这类虚词和标点，
    # 否则它们会因为高频而霸榜，但没有研究意义。
    stopwords=list(load_stopwords("zh_cl_sim")),
    # 只保留长度 >= 2 的词（作业要求），排除单字虚词和单字噪声。
    min_word_length=2,
    # 只保留「多重检验校正后」p 值 <= 0.05 的搭配词，即统计显著。
    max_adjusted_p=0.05,
)

# 要计算并输出的关联度量：
#   log_likelihood = 显著度（偏高频词）
#   logDice        = 强度（偏紧绑词对，范围 0~14）
MEASURES = ["log_likelihood", "logDice"]


def main():
    # 确保输出目录存在（不存在就创建，exist_ok=True 表示已存在也不报错）
    os.makedirs(OUTDIR, exist_ok=True)

    # 语料对象：每次遍历都会重新打开文件，所以可被反复扫描
    corpus = SegmentedCorpus()

    # 逐个运行三种设置
    for name, options in RUNS:
        # 核心调用：找 TARGET 的搭配词。
        # **options 会把 method/horizon 展开成关键字参数传进来。
        df = find_collocates(
            corpus,                  # 分词语料（Iterable[list[str]]）
            TARGET,                  # 目标词
            measures=MEASURES,       # 额外输出 log_likelihood、logDice
            filters=FILTERS,         # 停用词 / 最短词长 / 显著性阈值
            correction="fdr_bh",     # 多重检验校正方法：Benjamini-Hochberg
            alternative="greater",   # 只检验“吸引”（共现多于偶然），不管“排斥”
            sort_by="log_likelihood",# 结果按显著度排序
            **options,
        )

        # 每个设置存成一个独立 CSV（作业要求：一次运行一个 CSV）
        df.to_csv(os.path.join(OUTDIR, f"collocates_{name}.csv"), index=False)

        # ── 下面只是把重点打印到屏幕上，方便快速查看 ──
        # 分别按两种度量取前 10，看它们排出来的词是否一致
        top_ll = df.sort_values("log_likelihood", ascending=False).head(10)
        top_ld = df.sort_values("log_dice", ascending=False).head(10)

        # Spearman 相关系数：两种排序的一致程度（1=完全一致，0=无关）
        rho = df["log_likelihood"].rank().corr(df["log_dice"].rank())

        print(f"\n===== {name}: {len(df)} significant collocates =====")
        print("top-10 log-likelihood:", ", ".join(top_ll["collocate"]))
        print("top-10 logDice       :", ", ".join(top_ld["collocate"]))
        print(f"Spearman rho = {rho:.2f}")


# 只有当本文件被直接运行（python code/collocations.py）时才执行 main，
# 被其它文件 import 时不会自动运行。
if __name__ == "__main__":
    main()
