# Included Data and Examples
<details><summary><strong>Business Analytics<strong></summary>
<p>

- [Hillstrom Email Marketing](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html)
  - Is directly downloaded and formatted with CauseInfer [(see script)](https://github.com/andrewtavis/causeinfer/blob/master/causeinfer/data/hillstrom.py).
  - [Example notebook](https://github.com/andrewtavis/causeinfer/blob/master/examples/business_hilstrom.ipynb) (in progress).

```python
from causeinfer.data import hillstrom
hillstrom.download_hillstrom()
data_hillstrom = hillstrom.load_hillstrom(user_file_path="datasets/hillstrom.csv",
                                          format_covariates=True, 
                                          normalize=True)

df = pd.DataFrame(data_hillstrom["dataset_full"], 
                  columns=data_hillstrom["dataset_full_names"])
```
# 
- [Criterio Uplift](https://ailab.criteo.com/criteo-uplift-prediction-dataset/)
  - Download and formatting script in progress.
  - Example notebook to follow.

</p>
</details>

<details><summary><strong>Medical Trials<strong></summary>
<p>

- [Mayo Clinic PBC](https://www.mayo.edu/research/documents/pbchtml/DOC-10027635)
  - Is directly downloaded and formatted with CauseInfer [(see script)](https://github.com/andrewtavis/causeinfer/blob/master/causeinfer/data/mayo_pbc.py).
  - [Example notebook](https://github.com/andrewtavis/causeinfer/blob/master/examples/medical_mayo_pbc.ipynb) (in progress).

```python
from causeinfer.data import mayo_pbc
mayo_pbc.download_mayo_pbc()
data_mayo_pbc = mayo_pbc.load_mayo_pbc(user_file_path="datasets/mayo_pbc.text",
                                       format_covariates=True, 
                                       normalize=True)

df = pd.DataFrame(data_mayo_pbc["dataset_full"], 
                  columns=data_mayo_pbc["dataset_full_names"])
```
# 
- [Pintilie Tamoxifen](https://onlinelibrary.wiley.com/doi/book/10.1002/9780470870709)
  - Accompanied the linked text, but is now unavailable. It is provided in the [datasets directory](https://github.com/andrewtavis/causeinfer/tree/master/causeinfer/data/datasets) for direct download.
  - Formatting script in progress.
  - Example notebook to follow.

</p>
</details>

<details><summary><strong>Socio-economic Analysis<strong></summary>
<p>

- [CMF Microfinance](https://www.aeaweb.org/articles?id=10.1257/app.20130533)
  - Accompanied the linked text, but is now unavailable. It is provided in the [datasets directory](https://github.com/andrewtavis/causeinfer/tree/master/causeinfer/data/datasets) for direct download.
  - Is formatted with CauseInfer [(see script)](https://github.com/andrewtavis/causeinfer/blob/master/causeinfer/data/cmf_microfinance.py).
  - [Example notebook](https://github.com/andrewtavis/causeinfer/blob/master/examples/socio_econ_cmf_micro.ipynb) (in progress).

```python
from causeinfer.data import cmf_micro
data_cmf_micro = cmf_micro.load_cmf_micro(user_file_path="datasets/cmf_micro",
                                          format_covariates=True, 
                                          normalize=True)

df = pd.DataFrame(data_cmf_micro["dataset_full"], 
                  columns=data_cmf_micro["dataset_full_names"])
```
# 
- [Lalonde Job Training](https://users.nber.org/~rdehejia/data/.nswdata2.html)
  - Download and formatting script in progress.
  - Example notebook to follow.

</p>
</details>

<details><summary><strong>Simmulated Data<strong></summary>
<p>

- Work is currently being done to add a data generator, thus allowing for theoretical tests with known treatmet effects. 
- Example notebook to follow.

</p>
</details>