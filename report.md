# Understanding Collocations of 内阁 in the Mingshi

zhangmin

Keywords: 内阁; corpus; collocation; Mingshi

## Abstract

This report takes the Mingshi as a corpus and seeks to understand the institution 内阁 by identifying the words that co-occur with it. The study has three steps: first, it finds the words that co-occur significantly with 内阁, and their expected values and p-values are used to judge significance; second, KWIC is used to return to the collocates' original sentences and verify their contexts by 卷; third, the meaning of these words in context is analysed in order to understand the importance of 内阁 in the Ming dynasty.

## 1. Introduction

The Mingshi is an official history compiled at the Qing court. As is well known, in the early Ming Zhu Yuanzhang abolished the office of chancellor, and it was only under the Yongle emperor (Chengzu) that 内阁 was established. What important role, then, did 内阁 play in the Ming? Many scholars have offered their own interpretations from textual sources. In this report, we use a collocation approach to examine the words that co-occur frequently with the keyword 内阁, and then use KWIC to return to their original sentences. By analysing the meaning of these collocates in context, we can examine the role and main duties of 内阁 as an institution.

## 2. Method

### 2.1 Building the corpus

It must first be clear that a collocate is a word that co-occurs with 内阁 more often than chance; the criterion is not "high frequency" but "observed co-occurrence above random expectation". The Mingshi was then segmented: the whole text yields 170,503 sentences and 2,095,352 tokens, in which 内阁 appears 297 times—the unit of all later statistics. A context window was taken around every 内阁 to find stable collocates, set at 5 and 10. The results show that the top four—机务, 学士, 拟旨, 中书—are stable across both windows, while the fifth changes with the window and the measure: at window 5 it is 参预; at window 10 it is 吏部 by log-likelihood and 舍人 by logDice. The p-values of 机务, 中书, 拟旨 and 参预 underflow to 0 (not literally zero, but smaller than the computer can represent), and they are highly significant; 舍人 has an adjusted p-value of 5.3×10⁻⁷, still below 0.05, and is therefore significant.

### 2.2 Analysing the contexts

机务, one of the most frequent collocates, means "confidential state affairs": "卷七十四：命内阁学士典机务，诏册、制诰皆属之。" "卷十：乙亥，侍讲学士马愉、侍讲曹鼐入阁预机务。" "卷一百七十一：即日命有贞兼学士，入内阁，参预机务。" "卷二百二十九：文皇帝始置内阁，参预机务。" The text shows that the main task of 内阁 was to assist the emperor and take part in confidential government business.

学士 is also central. What does it mean? "卷七十二：景泰中，左都御史王文升吏部尚书，兼学士，入内阁……" "卷一百七十一：命有贞兼学士，入内阁，参预机务。" "卷九十四：仁宗特命内阁学士会审重囚。" It is thus both a qualification for entering 内阁 and a form of address for its members. 学士 is a Hanlin literary-official title and the qualification post for entering 内阁; because the text repeatedly writes 内阁学士 and 兼学士入内阁, it became a frequent collocate—showing that members of 内阁 came from the Hanlin Academy and were "literary officials".

拟旨 is another frequent collocate. "卷二百三十一：内阁代言拟旨，本顾问之遗，遇有章奏，阁臣宜各拟一旨。" "卷二百五十：帝亦为心动，令内阁拟旨。" "卷二百五十三：帝令拟谕，国观乃拟旨以进。" Drafting edicts was thus the core duty of 内阁. But this power was not constant: "卷二百四十二：比来拟旨不由内阁，托以亲裁。" (the emperor bypassed 内阁); "卷二百〇七：拟旨间出于中人，奸谀渐幸于左右。" (eunuchs interfered); "卷一百九十六：拟旨不密……若天子权在其掌握。" (a minister was accused of monopolising it). The right to draft edicts thus changed in the struggle with eunuch power.

中书 is likewise frequent. "卷七十四：正统后，学士不能视诰敕，内阁悉委于中书、序班、译字等官。" "卷八十六：崇祯十二年，崇明人沈廷扬为内阁中书，复陈海运之便，且辑《海运书》。" Here 中书 is the subordinate clerk (中书舍人) of 内阁, who copied edicts and handled documents.

## 3. Results

Across the three runs the number of significant collocates rose from 548 (window 5) to 744 (window 10) to 1001 (sentence). This is expected: a wider window offers more co-occurrence opportunities, so more words qualify. A stable core appears in every run—机务, 中书, 学士, 拟旨, 六部, 九卿, 舍人—and, because it does not depend on the window or on the measure, it is the most reliable evidence that the Mingshi defines 内阁 through its functions and its place in government. Words that appear only in the narrow window include 票拟, 诏举 and 翰林学士; words that appear only at the sentence level include 六科, 御史, 五府, 礼部 and 廷推. The former describe the immediate functions of 内阁, while the latter describe the institutions and figures that appear alongside it in the same passage. The two measures agree closely (Spearman rho = 0.85, 0.79, 0.80) but diverge on particular items: logDice promotes tightly bound words such as 拟旨 and 舍人, whereas log-likelihood promotes the frequent word 吏部. Significance, moreover, is not the same as importance: 九卿 has only 6 co-occurrences but an expected value of 0.12 (about 52 times chance), while 舍人 has 6 co-occurrences against an expectation of 0.24. Several high-ranked items—一送, 官入, 专用词—are segmentation artifacts and are not interpreted.

## 4. Interpretation

The collocates suggest that the Mingshi presents 内阁 less as an isolated centre of power than as one institution within a cluster of central government bodies. This is most visible in its association with 六部 and 九卿. 六部 co-occurs with 内阁 six or seven times (O = 6–7), against an expected value of only E ≈ 0.10–0.16—about 50–60 times chance—and ranks between 6th and 11th. "卷五十三：内阁、五府、六部奏事官……" and "卷一百八十九：祖宗设内阁、六部，赞万几，理庶务，职至重也。" show that 六部 and 内阁 were both central administrative institutions that worked alongside one another. "卷一百七十：请六部大事同内阁奏行" states this most directly: major matters of the 六部 were to be reported jointly with 内阁. The two were thus partners in government rather than a clear hierarchy.

九卿 co-occurs with 内阁 only six times (seven under the sentence method). In absolute terms this is not much—fewer than 机务 (15) or 学士 (10–12)—but 九卿 appears only 106 times in the whole text and its expected value is just 0.12, so six co-occurrences are already rare (about 52 times the expectation). It is therefore significant and ranks high (7th–13th). The text again clarifies the relationship: "卷十三：诏内阁九卿考核天下方面官。" and "卷二十三：召对内阁、九卿、科道及入觐两司官于文华殿。" Like 六部, 九卿 stood alongside 内阁 in the process of deliberation and administration rather than below it; both ultimately served the emperor. Taken together, 六部 and 九卿 show that 内阁 was framed as a participant in a collective machinery of government—deliberating, reporting and jointly deciding with the other central agencies—rather than as a self-standing rival to the throne.

## 5. Limitations

Three limits qualify these findings. First, jieba uses a modern dictionary and mis-segments this classical text, merging or splitting words incorrectly (for example 官入, 一送 and 专用词), and it splits 中书舍人 into 中书 and 舍人, which inflates their frequency. Second, several collocates are ambiguous: 中书 can mean the clerks of 内阁 or the earlier 中书省; 机务 also occurs in the Nanjing office 参赞机务; 学士 can refer to Hanlin scholars outside 内阁; and 舍人 can mean 侍仪舍人, a ritual official. Only occurrences in the same sentence as 内阁 were used. Third, the tail of the list depends on the window, so only the cross-window core is reliable; moreover, some collocations rest on very few tokens—九卿 co-occurs with 内阁 only six or eight times—so a single segmentation error could change the result. Finally, collocations reveal the framing of the text, not causation, and the *Mingshi* is a Qing-court product with its own judgements. A different target (for example 首辅 or 司礼监) or a different part of the text would yield a different picture.
