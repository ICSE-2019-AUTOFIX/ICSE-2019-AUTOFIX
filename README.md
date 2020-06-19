# DLFix: Context-based Code Transformation Learning for Automated Program Repair

Automated Program Repair (APR) is very useful in helping developers
in the process of software development and maintenance. Despite
recent advances in deep learning (DL), the DL-based APR approaches
still have limitations in learning bug-fixing code changes
and the context of the surrounding source code of the bug-fixing
code changes. These limitations lead to incorrect fixing locations
or fixes. In this paper, we introduce DLFix, a two-tier DL model
that treats APR as code transformation learning from the prior bug
fixes and the surrounding code contexts of the fixes. The first layer
is a tree-based RNN model that learns the contexts of bug fixes and
its result is used as an additional weighting input for the second
layer designed to learn the bug-fixing code transformations.
We conducted several experiments to evaluate DLFix in two
benchmarks: Defect4J and Bugs.jar, and a newly built bug datasets
with a total of +20K real-world bugs in eight projects.We compared
DLFix against a total of 13 state-of-the-art pattern-based APR tools.
Our results show that DLFix can auto-fix more bugs than 11 of
them, and is comparable and complementary to the top two patternbased
APR tools in which there are 7 and 11 unique bugs that they
cannot detect, respectively, but we can. Importantly, DLFix is fully
automated and data-driven, and does not require hard-coding of
bug-fixing patterns as in those tools. We compared DLFix against 4
state-of-the-art deep learning based APR models. DLFix is able to
fix 2.5 times more bugs than the best performing baseline.

----------
# Data Set

In our paper, we used three datasets to evaluate our work with baselines. All these three datasets are from existing works.

To train the model, we use the dataset BigFix from the paper: 
https://2019.splashcon.org/details/splash-2019-oopsla/46/Improving-Bug-Detection-via-Context-Based-Code-Representation-Learning-and-Attention-
With the data from:
https://github.com/OOPSLA-2019-BugDetection/OOPSLA-2019-BugDetection

To evaluate the performance between our approach and pattern based baselines, we use the dataset Defects4J:
https://dl.acm.org/doi/10.1145/2610384.2628055
With the data from:
https://github.com/rjust/defects4j

To evaluate the performance between our approach and deep learning based baselines, we use the dataset BigFix and Bugs.jar which is:
https://dl.acm.org/doi/10.1145/3196398.3196473
With the data from:
https://github.com/bugs-dot-jar/bugs-dot-jar


