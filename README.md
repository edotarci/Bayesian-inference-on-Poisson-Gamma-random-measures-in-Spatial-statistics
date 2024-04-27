This repository contains the report and the code for my bachelor's final project (worth 3 ECTS). 
The report (pdf file) is meant to be shared while the code is just the implementation of the algorithms presented in the paper;

\section*{Abstract} % Titolo dell'abstract senza numerazione

In this bachelor's final project, we begin by providing some background on Random Measures, with a focus on Poisson Point Processes, Completely Random Measures, and Gamma Processes. Then, the Poisson-Gamma Random Measure, a shot noise Cox process, is introduced and theorems for its simulation are presented. Additionally, we offer illustrative examples along with numerical methodologies to facilitate implementation. 

This stochastic process is well-suited for explaining and modeling point processes occurring on subsets of $\mathbb{R}^2$ where clustering is notable, such as in instances of forest fires, taxi pickups, and violent crimes.

In the second section, a concise overview of Markov Chain Monte Carlo (MCMC) algorithms is provided, with an emphasis on methodologies relevant to the subsequent discussion.

In the third segment, we present our contribution to the topic: the development of a Bayesian inference algorithm tailored specifically for Poisson-Gamma Random Measures.

A more generalized model for Bayesian inference on such measures has already been proposed in \cite{ref4}. Nonetheless, we introduce an alternative approach based on discretizing the underlying Gamma process, namely a discrete Gamma process. We are confident that our model offers computational advantages, increased stability, and enables sampling from the posterior while observing multiple realizations of the same process simultaneously (unlike in \cite{ref4}, where only one realization is considered). Additionally, we will present a partial result demonstrating the efficacy of our model in Bayesian inference, even in cases where the latent Gamma process is non-discrete.


Finally, we demonstrate the practical application of our approach using georeferenced wildfire data. This application serves to showcase the properties of the model and inference techniques, both in a constant context and on a time-varying scale.
