CIG软件列表
###########

:date: 2014-02-02 00:30
:author: SeisMan
:category: 地球物理相关资源
:tags: 网站, 理论地震图
:slug: cig-software-library

.. contents::

CIG，Computational Infrastructure for Geodynamics。

主页： http://www.geodynamics.org/

软件下载： http://www.geodynamics.org/cig/software

Github项目主页： https://github.com/geodynamics

网站提供的软件包分类如下：

Short-Term Crustal Dynamics
===========================

-  PyLith：地壳形变的动态和准静态模拟；1D、2D、3D；有限元；串行、并行；用于研究地震和火山；
-  RELAX：evaluates the displacement and stress in a half space with gravity due to dislocations, Mogi sources, and surface tractions; and the nonlinear time-dependent deformation that follows due to power-law rheology materials in the bulk and/or rate-strengthening friction faults.
-  SELEN：solves numerically the so-called "Sea Level Equation" (SLE) for a spherical, layered, non-rotating Earth with Maxwell viscoelastic rheology.
-  LithoMop：岩石圈形变模拟；粘弹/塑性变形；有限元；PyLith的原始版本；

Long-Term Tectonics
===================

-  Gale：2D/3D code for the long-term tectonics community. The code solves problems related to orogenesis, rifting, and subduction with coupling to surface erosion models.
-  Plasti：2D ALE (Arbitrary Lagrangian Eulerian) code donated to CIG by Sean Willett and Chris Fuller of the University of Washington. The code originated at Dalhousie University in Canada.
-  SNAC：Updated Lagrangian explicit finite difference code for modeling a finitely deforming elasto-visco-plastic solid in 3D.

Mantle Convection
=================

-  Aspect：Finite element parallel code to simulate problems in thermal convection in both 2D and 3D models - currently in alpha testing.
-  CitcomCU：Finite element parallel code capable of modeling thermochemical convection in a three dimensional domain appropriate for convection within the Earth's mantle.
-  CitcomS：Finite element code designed to solve compressible thermochemical convection problems relevant to Earth's mantle.
-  ConMan：Finite element program for the solution of the equations of incompressible, infinite-Prandtl number convection in two dimensions, originally written by Scott King, Arthur Raefsky, and Brad Hager.
-  Ellipsis3d：Three-dimensional version of the particle-in-cell finite element code Ellipsis, a solid modeling code for visco-elastoplastic materials. The particle-in-cell method combines the strengths of the Lagrangian and Eulerian formulations of mechanics while bypassing their limitations.
-  HC：Global mantle circulation solver following Hager & O'Connell (1981) which can compute velocities, tractions, and geoid for simple density distributions and plate velocities.

Seismology
==========

-  Specfem3D：地震波波传播模拟；谱元法；3D沉积盆地；
-  Specfem3D Globe：地震波波场模拟；全球或大区域；3D；谱元法；
-  Specfem3D Geotech：谱元法；3D slope stability analysis and simulation of 3D multistage excavation；
-  Specfem2D：谱元法；2D；波场模拟；acoustic、(an)elastic、poroelastic or coupled acoustic-(an)elastic-poroelastic media.
-  Specfem1D：谱元法；波场模拟；1D；演示代码；
-  Mineos：合成地震图；1D模型；球对称非旋转地球模型；normal mode summation.
-  Flexwin：Automates the time-window selection problem for seismologists. It operates on pairs of observed and synthetic single component seismograms, defining windows that cover as much of a given seismogram as possible, while avoiding portions of the waveform that are dominated by noise.
-  Seismic CPML：Eight open-source Fortran90 programs to solve the two-dimensional or three-dimensional isotropic or anisotropic elastic, viscoelastic or poroelastic wave equation using a finite-difference method with Convolutional Perfectly Matched Layer (C-PML) conditions；
-  Finite-Frequency Tomography Software：For the programs documented in Nolet, G., A Breviary of Seismic Tomography (CUP, 2008).

Geodynamo
=========

-  Calypso：Set of codes for parallel magnetohydrodynamics dynamo simulation in a rotating spherical shell using spherical harmonics expansion methods.
-  MAG：Serial version of a rotating spherical convection/magnetoconvection/dynamo code, developed by Gary Glatzmaier and modified by Uli Christensen and Peter Olson.

Computational Science
=====================

-  Geodynamics AMR Suite (deal.II)：C++ program library targeted at the computational solution of partial differential equations using adaptive finite elements. Its state-of-the-art programming techniques offer a modern interface to the complex data structures and algorithms required. CIG has sponsored Wolfgang Bangerth (Texas A&M) to produce tutorials that use deal.II in various implementations.
-  Cigma：Suite of tools that facilitates the comparison of numerical models, and performs error analysis, benchmarking, and code verification.
-  Exchanger：Package containing several C++ base classes. These classes, when customized for a solver, can provide communication channels between solvers. This packaged is used by CitcomS for solver coupling.
-  Pythia/Pyre：Pyre framework and a collection of packages that interact with it, such as an interface to the ACIS solid modeling package.
