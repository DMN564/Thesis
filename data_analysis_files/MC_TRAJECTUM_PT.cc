// -*- C++ -*-
#include "Rivet/Analysis.hh"
#include "Rivet/Projections/FinalState.hh"
#include "Rivet/Projections/FastJets.hh"
#include <cmath>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>

namespace Rivet {

class MC_TRAJECTUM_PT : public Analysis {
public:

  RIVET_DEFAULT_ANALYSIS_CTOR(MC_TRAJECTUM_PT);

  void init() {

    const FinalState fs(Cuts::abseta < 5.0);
    FastJets jetfs(fs, FastJets::ANTIKT, 0.4);
    declare(jetfs, "jets");

    book(_nEvt,        "N_EVENTS");
    book(_nEvtLowQ2,   "N_EVENTS_LOW_Q2");
    book(_nEvtHighQ2,  "N_EVENTS_HIGH_Q2");
    book(_nEvtLowEcc,  "N_EVENTS_LOW_ECC");
    book(_nEvtHighEcc, "N_EVENTS_HIGH_ECC");

    // Histogram pointers
    _q2                             = _h["Q2"];

    _pT50                           = _h["P_t_50"];
    _pT50LowQ2                      = _h["P_t_50_Low_Q2"];
    _pT50HighQ2                     = _h["P_t_50_High_Q2"];

    _pT50InPlane_final              = _h["P_t_50_In_Plane_Final"];
    _pT50InPlaneLowQ2               = _h["P_t_50_In_Plane_Low_Q2"];
    _pT50InPlaneHighQ2              = _h["P_t_50_In_Plane_High_Q2"];

    _pT50OutPlane_final             = _h["P_t_50_Out_Plane_Final"];
    _pT50OutPlaneLowQ2              = _h["P_t_50_Out_Plane_Low_Q2"];
    _pT50OutPlaneHighQ2             = _h["P_t_50_Out_Plane_High_Q2"];

    _eccentricity                   = _h["Ecc"];

    _pT50LowEccentricity            = _h["P_t_50_Low_Ecc"];
    _pT50HighEccentricity           = _h["P_t_50_High_Ecc"];

    _pT50InPlane_initial            = _h["P_t_50_In_Plane_Initial"];
    _pT50InPlaneLowEccentricity     = _h["P_t_50_In_Plane_Low_Ecc"];
    _pT50InPlaneHighEccentricity    = _h["P_t_50_In_Plane_High_Ecc"];

    _pT50OutPlane_initial           = _h["P_t_50_Out_Plane_Initial"];
    _pT50OutPlaneLowEccentricity    = _h["P_t_50_Out_Plane_Low_Ecc"];
    _pT50OutPlaneHighEccentricity   = _h["P_t_50_Out_Plane_High_Ecc"];

    // Booking
    book(_q2, "Q2", 1000, 0, 7);

    book(_pT50, "P_t_50", 10, 50, 120);
    book(_pT50LowQ2, "P_t_50_Low_Q2", 10, 50, 120);
    book(_pT50HighQ2, "P_t_50_High_Q2", 10, 50, 120);

    book(_pT50InPlane_final, "P_t_50_In_Plane_Final", 10, 50, 120);
    book(_pT50InPlaneLowQ2, "P_t_50_In_Plane_Low_Q2", 10, 50, 120);
    book(_pT50InPlaneHighQ2, "P_t_50_In_Plane_High_Q2", 10, 50, 120);

    book(_pT50OutPlane_final, "P_t_50_Out_Plane_Final", 10, 50, 120);
    book(_pT50OutPlaneLowQ2, "P_t_50_Out_Plane_Low_Q2", 10, 50, 120);
    book(_pT50OutPlaneHighQ2, "P_t_50_Out_Plane_High_Q2", 10, 50, 120);

    book(_eccentricity, "Ecc", 1000, 0, 1);

    book(_pT50LowEccentricity, "Jet_P_t_50_Low_Ecc", 10, 50, 120);
    book(_pT50HighEccentricity, "Jet_P_t_50_High_Ecc", 10, 50, 120);

    book(_pT50InPlane_initial, "P_t_50_In_Plane_Initial", 10, 50, 120);
    book(_pT50InPlaneLowEccentricity, "P_t_50_In_Plane_Low_Ecc", 10, 50, 120);
    book(_pT50InPlaneHighEccentricity, "P_t_50_In_Plane_High_Ecc", 10, 50, 120);

    book(_pT50OutPlane_initial, "P_t_50_Out_Plane_Initial", 10, 50, 120);
    book(_pT50OutPlaneLowEccentricity, "P_t_50_Out_Plane_Low_Ecc", 10, 50, 120);
    book(_pT50OutPlaneHighEccentricity, "P_t_50_Out_Plane_High_Ecc", 10, 50, 120);

    // Load external event data
    std::ifstream file("/export/users/dahamvin/hydrohepmcs/event_analysis_filtered.txt");

    std::string line;
    while (std::getline(file, line)) {
      if (line.empty() || line[0] == '#') continue;

      std::istringstream iss(line);
      int event_id;
      double q2, psi_ep, epsilon2, phi2;

      if (iss >> event_id >> q2 >> psi_ep >> epsilon2 >> phi2) {
        eventMap[event_id] = {epsilon2, q2, psi_ep, phi2};
      }
    }
  }

  void analyze(const Event& event) {
    auto hi = event.genEvent()->heavy_ion();
    if (!hi) vetoEvent;

    int eventID = hi->Ncoll_hard();
    auto it = eventMap.find(eventID);
    if (it == eventMap.end()) vetoEvent;

    const EventData& ev = it->second;

    double q2 = ev.Q2;
    double eccentricity = ev.epsilon;
    double psi2_ep = ev.psi_ep;
    double psi2_pp = ev.phi_2 + DEG_90;



    _q2->fill(q2);
    _eccentricity->fill(eccentricity);

    bool hasLowQ2  = q2 < 1.937;
    bool hasHighQ2 = q2 > 3.930;

    bool hasLowEcc  = eccentricity < 0.336;
    bool hasHighEcc = eccentricity > 0.564;


    Jets jets = apply<FastJets>(event, "jets")
        .jetsByPt(Cuts::pT > 50 * GeV);

    if (jets.empty()) vetoEvent;

    _nEvt->fill();
    if (hasLowQ2)  _nEvtLowQ2->fill();
    if (hasHighQ2) _nEvtHighQ2->fill();
    if (hasLowEcc)  _nEvtLowEcc->fill();
    if (hasHighEcc) _nEvtHighEcc->fill();

    for (const Jet& jet : jets) {

      double pT = jet.pT() / GeV;
      double phi = jet.phi();

      double dphi_final = std::fmod(phi - psi2_ep + DEG_180, DEG_360);
      double dphi_init  = std::fmod(phi - psi2_pp + DEG_180, DEG_360);

      if (dphi_final < 0) dphi_final += DEG_360;
      if (dphi_init  < 0) dphi_init  += DEG_360;

      dphi_final -= DEG_180;
      dphi_init  -= DEG_180;

      dphi_final = std::fabs(dphi_final);
      dphi_init  = std::fabs(dphi_init);

      bool in_final  = (dphi_final < DEG_30 || dphi_final > DEG_150);
      bool out_final = (dphi_final > DEG_60 && dphi_final < DEG_120);

      bool in_init  = (dphi_init < DEG_30 || dphi_init > DEG_150);
      bool out_init = (dphi_init > DEG_60 && dphi_init < DEG_120);

      // Final state
      if (in_final) {
        _pT50InPlane_final->fill(pT);
        if (hasLowQ2){
           _pT50InPlaneLowQ2->fill(pT);
        }else if (hasHighQ2){
           _pT50InPlaneHighQ2->fill(pT);
        }
      }

      else if (out_final) {
        _pT50OutPlane_final->fill(pT);
        if (hasLowQ2){
           _pT50OutPlaneLowQ2->fill(pT);
        }else if (hasHighQ2){
          _pT50OutPlaneHighQ2->fill(pT);
        }
      }

      // Initial state
      if (in_init) {
        _pT50InPlane_initial->fill(pT);
        if (hasLowEcc){
           _pT50InPlaneLowEccentricity->fill(pT);
        } else if (hasHighEcc){
          _pT50InPlaneHighEccentricity->fill(pT);
        }
      }

      else if (out_init) {
        _pT50OutPlane_initial->fill(pT);
        if (hasLowEcc){
           _pT50OutPlaneLowEccentricity->fill(pT);
        }else if (hasHighEcc){
          _pT50OutPlaneHighEccentricity->fill(pT);
        }
      }

      // Inclusive
      _pT50->fill(pT);

      if (hasLowQ2) {
          _pT50LowQ2->fill(pT);
      } else if (hasHighQ2){
        _pT50HighQ2->fill(pT);
      }

      if (hasLowEcc) {
        _pT50LowEccentricity->fill(pT);
      } else if (hasHighEcc){
        _pT50HighEccentricity->fill(pT);
      }
    }
  }

  void finalize() {

    double scaleFactor = crossSection() / picobarn / sumW();

    normalize(_q2);
    normalize(_eccentricity);

    scale(_pT50, scaleFactor);
    scale(_pT50LowQ2, scaleFactor);
    scale(_pT50HighQ2, scaleFactor);

    scale(_pT50LowEccentricity, scaleFactor);
    scale(_pT50HighEccentricity, scaleFactor);

    scale(_pT50InPlane_final, scaleFactor);
    scale(_pT50OutPlane_final, scaleFactor);

    scale(_pT50InPlane_initial, scaleFactor);
    scale(_pT50OutPlane_initial, scaleFactor);

    scale(_pT50InPlaneLowQ2, scaleFactor);
    scale(_pT50InPlaneHighQ2, scaleFactor);
    scale(_pT50OutPlaneLowQ2, scaleFactor);
    scale(_pT50OutPlaneHighQ2, scaleFactor);

    scale(_pT50InPlaneLowEccentricity, scaleFactor);
    scale(_pT50InPlaneHighEccentricity, scaleFactor);
    scale(_pT50OutPlaneLowEccentricity, scaleFactor);
    scale(_pT50OutPlaneHighEccentricity, scaleFactor);
  }

private:

  const double DEG_30  = M_PI/6;
  const double DEG_60  = M_PI/3;
  const double DEG_90  = M_PI/2;
  const double DEG_120 = 2*M_PI/3;
  const double DEG_150 = 5*M_PI/6;
  const double DEG_180 = M_PI;
  const double DEG_360 = 2*M_PI;

  map<string, Histo1DPtr> _h;

  CounterPtr _nEvt, _nEvtLowQ2, _nEvtHighQ2;
  CounterPtr _nEvtLowEcc, _nEvtHighEcc;

  Histo1DPtr _q2, _pT50, _pT50LowQ2, _pT50HighQ2;
  Histo1DPtr _pT50InPlane_final, _pT50OutPlane_final;
  Histo1DPtr _pT50InPlaneLowQ2, _pT50InPlaneHighQ2;
  Histo1DPtr _pT50OutPlaneLowQ2, _pT50OutPlaneHighQ2;

  Histo1DPtr _eccentricity, _pT50LowEccentricity, _pT50HighEccentricity;
  Histo1DPtr _pT50InPlane_initial, _pT50OutPlane_initial;
  Histo1DPtr _pT50InPlaneLowEccentricity, _pT50InPlaneHighEccentricity;
  Histo1DPtr _pT50OutPlaneLowEccentricity, _pT50OutPlaneHighEccentricity;

  struct EventData {
    double epsilon, Q2, psi_ep, phi_2;
  };

  std::unordered_map<int, EventData> eventMap;
};

RIVET_DECLARE_PLUGIN(MC_TRAJECTUM_PT);

}
