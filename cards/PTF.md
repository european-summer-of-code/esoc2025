

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
The project is sponsored by [Fondazione Bruno Kessler](https://www.fbk.eu/it/), [Digital Industry center](https://www.fbk.eu/it/digital-industry/), [DSIP unit](https://dsip.fbk.eu/) and  will be jointly mentored by the DSIP unit (Andrea Gobbi, main developer of [DSIPTS](https://github.com/agobbifbk/DSIPTS_PTF)) and from members from GC.OS (`PTF` and `sktime` library).
