# Bayesian inference on Poisson-Gamma random measures for spatial statistics
This repository contains the report (Thesis.Visconti.final.pdf) and the code for my bachelor's final project (worth 3 ECTS). 

The report (pdf file) is meant to be shared while the code (the implementation of the algorithms presented in the paper) is not commented nor optimized yet, as the focus of the project was on the development of the Metropolis-within-Gibbs algorithm (see abstract) presented in the report. 

## Abstract

In this Bachelor’s Thesis, we investigate the Poisson-Gamma Random Measure, a shot noise Cox process introduced by Wolpert and Ickstadt in [4]. We begin by providing some background on Random Measures, with a focus on Poisson Point Processes, Completely Random Measures, and Gamma Processes. Then, the Poisson-Gamma Random Measure is presented along with theorems for its simulation. Additionally, we offer illustrative examples along with numerical methodologies to facilitate implementation.

In the second section, an overview of Markov Chain Monte Carlo (MCMC) algorithms is provided, with an emphasis on methodologies relevant to the subsequent discussion.

In the third segment, we present our contribution: the development of a Bayesian inference algorithm tailored specifically for Poisson-Gamma Random Measures.
A general model for Bayesian inference on such random measures has already been pro- posed in [4]. Nonetheless, we introduce an alternative approach based on discretizing the underlying Gamma process, namely a discrete Gamma process. We are confident that our model offers computational advantages, increased stability, and enables sampling from the posterior while observing multiple realizations of the same process simultaneously (unlike in [4], where only one realization is considered). Additionally, we believe that a partial result can be proved to show the efficacy of our model even in cases where the latent Gamma process is non-discrete.

Finally, we demonstrate the practical application of our approach using georeferenced wildfire data. This example serves to showcase the properties of the model and inference techniques, both in a constant scale and on a time-varying scale.

