// -*- C++ -*-
#include "Rivet/Analysis.hh"
#include "Rivet/Projections/FastJets.hh"
#include "Rivet/Projections/FinalState.hh"
#include "Rivet/Tools/Cuts.hh"

#include <cmath>

namespace Rivet {

/// @brief Add a short analysis description here
class MC_GLAUBER_PT : public Analysis {
public:
    /// Constructor
    RIVET_DEFAULT_ANALYSIS_CTOR(MC_GLAUBER_PT);

    /// @name Analysis methods
    /// @{

    /// Book histograms and initialise projections before the run
    void init() {
        // Initialise and register projections

        // The basic final-state projection:
        // all final-state particles within
        // the given eta acceptance
        const FinalState fs(Cuts::abseta < 5.0);

        // The final-state particles declared above are clustered using FastJet with
        // the anti-kT algorithm and a jet-radius parameter 0.4
        // muons and neutrinos are excluded from the clustering
        FastJets jetfs(fs, FastJets::ANTIKT, 0.4);
        declare(jetfs, "jets");

        book(_nEvt,        "N_EVENTS");
        book(_nEvtLowEcc,  "N_EVENTS_LOW_ECC");
        book(_nEvtHighEcc, "N_EVENTS_HIGH_ECC");

        _eccentricity                 = _h["ecc"];

        _pT50LowHighEccentricity      = _h["P_t_50"];
        _pT50LowEccentricity          = _h["P_t_50_Low_ecc"];
        _pT50HighEccentricity         = _h["P_t_50_High_ecc"];

        _pT50InPlane                  = _h["P_t_50_In_Plane"];
        _pT50InPlaneLowEccentricity   = _h["P_t_50_In_Plane_Low_ecc"];
        _pT50InPlaneHighEccentricity  = _h["P_t_50_In_Plane_High_ecc"];

        _pT50OutPlane                 = _h["P_t_50_Out_Plane"];
        _pT50OutPlaneLowEccentricity  = _h["P_t_50_Out_Plane_Low_ecc"];
        _pT50OutPlaneHighEccentricity = _h["P_t_50_Out_Plane_High_ecc"];

        // Specify custom binnings
        book(
            _eccentricity,
            "ecc",
            100,
            0,
            2);

        book(
            _pT50LowHighEccentricity,
            "Jet_P_t_50",
            NUMBER_OF_BINS,
            MINIMUM_ENERGY_GEV,
            MAXIMUM_ENERGY_GEV);
        book(
            _pT50LowEccentricity,
            "Jet_P_t_50_Low_ecc",
            NUMBER_OF_BINS,
            MINIMUM_ENERGY_GEV,
            MAXIMUM_ENERGY_GEV);
        book(
            _pT50HighEccentricity,
            "Jet_P_t_50_High_ecc",
            NUMBER_OF_BINS,
            MINIMUM_ENERGY_GEV,
            MAXIMUM_ENERGY_GEV);

        book(
            _pT50InPlane,
            "P_t_50_In_Plane",
            NUMBER_OF_BINS,
            MINIMUM_ENERGY_GEV,
            MAXIMUM_ENERGY_GEV);
        book(
            _pT50InPlaneLowEccentricity,
            "P_t_50_In_Plane_Low_ecc",
            NUMBER_OF_BINS,
            MINIMUM_ENERGY_GEV,
            MAXIMUM_ENERGY_GEV);
        book(
            _pT50InPlaneHighEccentricity,
            "P_t_50_In_Plane_High_ecc",
            NUMBER_OF_BINS,
            MINIMUM_ENERGY_GEV,
            MAXIMUM_ENERGY_GEV);

        book(
            _pT50OutPlane,
            "P_t_50_Out_Plane",
            NUMBER_OF_BINS,
            MINIMUM_ENERGY_GEV,
            MAXIMUM_ENERGY_GEV);
        book(
            _pT50OutPlaneLowEccentricity,
            "P_t_50_Out_Plane_Low_ecc",
            NUMBER_OF_BINS,
            MINIMUM_ENERGY_GEV,
            MAXIMUM_ENERGY_GEV);
        book(
            _pT50OutPlaneHighEccentricity,
            "P_t_50_Out_Plane_High_ecc",
            NUMBER_OF_BINS,
            MINIMUM_ENERGY_GEV,
            MAXIMUM_ENERGY_GEV);
    }

    /// Perform the per-event analysis
    void analyze(const Event &event) {
        auto eventHeavyIon = event.genEvent()->heavy_ion();

        if (!eventHeavyIon)
            vetoEvent;

        double eccentricity = eventHeavyIon->eccentricity();

        _eccentricity->fill(eccentricity);

        bool hasLowEccentricity  = eccentricity < 0.21;
        bool hasHighEccentricity = eccentricity > 0.47;

        // retrieve clustered jets, sorted by pT, with a minimum pT cut
        Jets eventJets50 = apply<FastJets>(event, "jets")
            .jetsByPt(Cuts::pT > MINIMUM_ENERGY_GEV * GeV);

        // veto event if there are no jets
        if (eventJets50.empty())
            vetoEvent;

        _nEvt->fill();
        if (hasLowEccentricity)  _nEvtLowEcc->fill();
        if (hasHighEccentricity) _nEvtHighEcc->fill();

        double planeAngle   = eventHeavyIon->event_plane_angle();

        for (auto jet : eventJets50) {
            double pT(jet.pT());
            double pTPerGeV = pT / GeV;
            double jetAngle(jet.momentum().phi());

            // normalize to [-π,π)
            double coneAngle = std::fmod(jetAngle - planeAngle + DEG_180, DEG_360);
            if (coneAngle < 0)
                coneAngle += DEG_360;
            coneAngle -= DEG_180;

            coneAngle = std::fabs(coneAngle);
            bool isInPlane  = (coneAngle < DEG_30 || DEG_150 < coneAngle);
            bool isOutPlane = (DEG_60 < coneAngle && coneAngle < DEG_120);

            if (isInPlane) {
                _pT50InPlane->fill(pTPerGeV);
            } else if (isOutPlane) {
                _pT50OutPlane->fill(pTPerGeV);
            }

            _pT50LowHighEccentricity->fill(pTPerGeV);

            if (hasLowEccentricity) {
                _pT50LowEccentricity->fill(pTPerGeV);
                if (isInPlane) {
                   _pT50InPlaneLowEccentricity->fill(pTPerGeV);
                } else if (isOutPlane) {
                   _pT50OutPlaneLowEccentricity->fill(pTPerGeV);
                }
            } else /*if (hasHighEccentricity)*/ {
                _pT50HighEccentricity->fill(pTPerGeV);
                if (isInPlane) {
                    _pT50InPlaneHighEccentricity->fill(pTPerGeV);
                } else if (isOutPlane) {
                    _pT50OutPlaneHighEccentricity->fill(pTPerGeV);
                }
            }
        }
    }

    /// Normalise histograms etc., after the run
    void finalize() {
        double crossSectionPerPicobarn = crossSection() / picobarn;
        double inverseScaleFactor      = crossSectionPerPicobarn / sumW();

        normalize(_eccentricity);

        scale(_pT50LowHighEccentricity, inverseScaleFactor);
        scale(_pT50LowEccentricity, inverseScaleFactor);
        scale(_pT50HighEccentricity, inverseScaleFactor);

        scale(_pT50InPlane, inverseScaleFactor);
        scale(_pT50OutPlane, inverseScaleFactor);

        scale(_pT50InPlaneHighEccentricity, inverseScaleFactor);
        scale(_pT50InPlaneLowEccentricity, inverseScaleFactor);
        scale(_pT50OutPlaneHighEccentricity, inverseScaleFactor);
        scale(_pT50OutPlaneLowEccentricity, inverseScaleFactor);
    }
    /// @}

    /// @name Histograms
    /// @{
    map<string, Histo1DPtr> _h;
    /// @}
private:
    const size_t NUMBER_OF_BINS     = 10;

    const double MINIMUM_ENERGY_GEV = 50;
    const double MAXIMUM_ENERGY_GEV = 120;

    const double DEG_30  = M_PI / 6;
    const double DEG_60  = M_PI / 3;
    const double DEG_120 = 2 * M_PI / 3;
    const double DEG_150 = 5 * M_PI / 6;
    const double DEG_180 = M_PI;
    const double DEG_360 = 2 * M_PI;

    double _sumLowHighEvents;
    double _sumLowEvents;
    double _sumHighEvents;

    double _sumInEvents;
    double _sumOutEvents;
    double _sumLowInEvents;
    double _sumHighInEvents;
    double _sumLowOutEvents;
    double _sumHighOutEvents;

    CounterPtr _nEvt, _nEvtLowEcc, _nEvtHighEcc;

    Histo1DPtr _eccentricity;
    Histo1DPtr _pT50LowHighEccentricity;
    Histo1DPtr _pT50LowEccentricity;
    Histo1DPtr _pT50HighEccentricity;
    Histo1DPtr _pT50InPlane;
    Histo1DPtr _pT50InPlaneHighEccentricity;
    Histo1DPtr _pT50InPlaneLowEccentricity;
    Histo1DPtr _pT50OutPlane;
    Histo1DPtr _pT50OutPlaneHighEccentricity;
    Histo1DPtr _pT50OutPlaneLowEccentricity;
};

RIVET_DECLARE_PLUGIN(MC_GLAUBER_PT);

} // namespace Rivet
