#ifndef SSDiLepAnalysis_XSAlgo_H
#define SSDiLepAnalysis_XSAlgo_H

// EL include(s):
#include <EventLoop/Algorithm.h>

// Infrastructure include(s):
#include "xAODRootAccess/Init.h"
#include "xAODRootAccess/TEvent.h"
#include "xAODRootAccess/TStore.h"
#include "AthContainers/AuxElement.h"
#include "AthLinks/ElementLink.h"

// EDM include(s):

// algorithm wrapper
#include "xAODAnaHelpers/Algorithm.h"

#include "LPXKfactorTool/LPXKfactorTool.h" 

// ROOT include(s):
#include "TH1D.h"

class XSAlgo : public xAH::Algorithm
{
  // put your configuration variables here as public variables.
  // that way they can be set directly from CINT and python.
public:

  bool m_doSomething;
  std::string m_systNameKfactorTool;
  float m_systValKfactorTool;

private:

  int m_numEvent;           //!
  int m_numObject;          //!
  int m_numEventPass;       //!
  int m_weightNumEventPass; //!
  int m_numObjectPass;      //!

  bool m_isMC;              //!
  bool m_isDerivation;      //!

  // cutflow
  bool  m_useCutFlow;       //!
  TH1D* m_cutflowHist;      //!
  TH1D* m_cutflowHistW;     //!
  int   m_cutflow_bin;      //!

  LPXKfactorTool*  m_p_kfactorTool; //!

  /* Initialise decorators */
  SG::AuxElement::Decorator< double >*        m_xsDecor;           //!
  SG::AuxElement::Decorator< double >*        m_FiltEffDecor;      //!
  SG::AuxElement::Decorator< double >*        m_KFactorNomDecor;      //!
  SG::AuxElement::Decorator< std::vector<float> >*        m_KFactorDecor;      //!
  SG::AuxElement::Decorator< std::vector<std::string> >*   m_KFactorDecorSys;   //!

  /* Initialise accessors */
  SG::AuxElement::Accessor< float >*         m_mcEvtWeightAcc;	   //!

  std::vector<CP::SystematicSet> m_systListKfactorTool; //!

  // variables that don't get filled at submission time should be
  // protected from being send from the submission node to the worker
  // node (done by the //!)
public:

  // this is a standard constructor
  XSAlgo ();

  ~XSAlgo();

  // these are the functions inherited from Algorithm
  virtual EL::StatusCode setupJob (EL::Job& job);
  virtual EL::StatusCode fileExecute ();
  virtual EL::StatusCode histInitialize ();
  virtual EL::StatusCode changeInput (bool firstFile);
  virtual EL::StatusCode initialize ();
  virtual EL::StatusCode execute ();
  virtual EL::StatusCode postExecute ();
  virtual EL::StatusCode finalize ();
  virtual EL::StatusCode histFinalize ();

  // this is needed to distribute the algorithm to the workers
  ClassDef(XSAlgo, 1);
};

#endif
