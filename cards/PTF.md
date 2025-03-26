

Join the Pytorch Forecasting team for a summer full of coding, learning and fun. Be part of our diverse community and join our efforts to advance deep learning and time series analysis capabilities, by helping create one of the first comprehensive time series DL toolboxes!


Participation is subject to the [sktime Code of Conduct](https://www.sktime.org/en/stable/get_involved/code_of_conduct.html).

In the remainder of this page:
- [Why PTF](WhyPTF?)
- The application process
  - [PTF application form](PFTapplication)
  - [Interview](Interview)
  - [Selection criteria](Selectioncriteria)
- [What we expect from you](Whatweexpectfromyou)
- [What you can expect from us](Whatyoucanexpectfromus)
- [Proposal Detail](ProposalDetail)
- [Mentors](Mentors)

## Why PTF?

Pytorch forecazsting ``PTF``, under the umbrella of `sktime`, aims to be a comprehensive and multipourpose deep learning-based time serie toolbox. In the version V2 we aim to extend the current implementation:
* adding SOTA multi output-multi multi-horizon time series forecasting DL models (encorder-decorder, foundational, customizable architectures)
* updating the list of loss functions and optimizers specifically designed for time series forecasting
* focusing on reproducibility (train-validation-test split, normalization, seeding)
* traking the training process for detecting over-under fitting 
* enanching the training procedure with hyperparameter-optimization functionalities
* implementing benchmarking between datasets and architectures
* exposing HPC's connectors 

The PTF V2 will be based on other open source projects such as [DSIPTS](https://github.com/agobbifbk/DSIPTS_PTF), [Time-Series-Library](https://github.com/thuml/Time-Series-Library) and [sktime](https://github.com/sktime/sktime).

**Are you ready for this?**



### PFT application 

**The deadline to complete all of these is April 7, 18:00 (UTC) and it starts by filling and submitting the PTF application form (link added here March 26)**.


After the deadline on April 7nd has passed, we will process the information provided and tell you the outcome no later than April 9th. There are two possible outcomes:
- Progress to interview. See below.
- Rejection. Though this will be disheartening for you, this is only a rejection for ESoC (which is particularly demanding of participants) and should not discourage you from pursuing open source contributions, either with PTF or another package.


### Interview
If successful in the above steps, we will invite you to a structured interview (ca. 30 minutes length; to be finalised) with core community members of sktime.
The interview will happen in the week period April 14 to 18, and our preferred dates is April 14. Please keep this date free if possible.

During the interview:
- we will ask you to give a short (5 to 10 minutes; to be finalised) presentation on a piece of Python code that you wrote that is related to **time series forecasting using pytorch**. Please be ready to screen share your code or to send a link to the repo containing your code.
- we will ask about your motivation to join PTF, your previous experience, your suitability for the specified project, and technical questions on data science and Python.

After the interview, we will rank the candidates and send a shortlist of our preferred candidates for reconciliation across participating institutions. 
We will inform you of *our* perspective on the interviews (see below for possible outcomes) at most one week after the final candidate is interviewed, and then we will inform you of the final decision by May 7.

When we inform you of the outcome of the interview, there are two possibilities:
* Conditional acceptance. This means you are in our shortlist sent to reconciliation across ESoC participating institutions. This means likely - but not guaranteed - acceptance.
* A rejection. This means you are not in our shortlist.
  - We understand this will be disheartening for you, but this is only a rejection for ESoC, which is particularly demanding of participants. We will always welcome anybody interested in joining sktime outside of ESoC.

### Selection criteria

In the above, the following are used for selection:

* experiences with deep learning (pytorch) applied to time series
* proeficency with common data science libraries and tools: pandas, polars, scikit-learn, hydra, lightening, aim, ...
* performance in the structured interview (for content see above)
* prior contributions to `sktime`, if applicable
* prior interactions with the community, if applicable

## What we expect from you

Our expectations for participants:
 * You are interested in time series, deep learning, AI, statistics, API design and software architecture.
 * You love coding in Python.
 * You are familiar with the basic data science ecosystem in Python, including numpy, pytorch, lightening, pandas/polars/dash and scikit-learn.
 * You enjoy working with a vibrant team of experienced DL scientists and software engineers.
 * You are enthusiastic about open-source.
 * You follow sktime [Code of Conduct](https://www.sktime.net/en/stable/get_involved/code_of_conduct.html).
* You maintain daily contact with your mentor(s).
* You engage with the sktime-PTF community and other mentees.



## What you can expect from us
The expectations on you are high, but you can expect just as much from us. You should expect:
* We follow the [Code of Conduct](https://www.sktime.net/en/stable/get_involved/code_of_conduct.html).
* 1-1 mentoring with an experienced contributor, with weekly meetings.
* Regular feedback and help on your efforts, including blogposts, with quick responses from us (usually respond within 2 working days).
* 'Agile' ways of working, used throughout the tech industry, e.g. daily standups.
* Cutting edge projects in highly sought-after areas of data science: time series, toolboxes, applications to healthcare and industry.
* The opportunity to acquire a variety of transferrable skills, both technical skills (like coding, design, testing, documentation) and soft skills (teamwork, giving and receiving feedback, goal setting).
* The opportunity to engage and socialise with the sktime community and other mentees.
* The opportunity to become a core developer of PTF.

## Proposal Detail

The selected candidate will:
* refactor some of the core functionalities of `PTF`:
    * data-layers: processing time series data in different sources: single csv, multiple csv, zarr files
    * dataloaders: standardizing the batch generation for groups of DL architectures (e.g. encoder-decorder, foundational)
    * model-layer: implementing common training-prediction procedures based on [lightning](https://lightning.ai/docs/pytorch/stable/)
* enrich the set of loss functions and optimizers
* add new functionalities:
    * benchmarking
    * optimization
    * HPC interface (for example using  [hydra](https://hydra.cc/docs/intro/) sweepers)

## Mentors
The project is sponsored by [Fondazione Bruno Kessler](https://www.fbk.eu/it/), [Digital Industry center](https://www.fbk.eu/it/digital-industry/), [DSIP unit](https://dsip.fbk.eu/) and  will be jointly mentored by the DSIP unit (Andrea Gobbi, main developer of [DSIPTS](https://github.com/agobbifbk/DSIPTS_PTF)) and from members from GOCS (`PTF` and `sktime` library).