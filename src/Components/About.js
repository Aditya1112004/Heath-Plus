import React from "react";
import Doctor from "../Assets/doctor-group.png";
import SolutionStep from "./SolutionStep";
import "../Styles/About.css";

function About() {
  return (
    <div className="about-section" id="about">
      <div className="about-image-content">
        <img src={Doctor} alt="Doctor Group" className="about-image1" />
      </div>

      <div className="about-text-content">
        <h3 className="about-title">
          <span>Contirbutors</span>
        </h3>
        <p className="about-description">
        "Each team member played a crucial role in bringing this project to life. Through collaboration, creativity, and dedication, we crafted an innovative solution designed to provide an exceptional user experience."
          </p>

        <h4 className="about-text-title">Your Solutions</h4>
        <SolutionStep
            title="Rida Shaikh"
            description={
              <>Explore My LinkedIn Profile for More Insights <br/> 
                <a href="https://www.linkedin.com/in/rida-shaikh-502928231/" target="_blank" rel="noopener noreferrer">
                  www.linkedin.com/in/rida-shaikh-502928231
                </a>
              </>
            }
          />
          <SolutionStep
              title="Nandini Pajgade"
              description={
                <>Explore My LinkedIn Profile for More Insights <br/> 
                  <a href="https://www.linkedin.com/in/nandini-pajgade-4a3351230/" target="_blank" rel="noopener noreferrer">
                    www.linkedin.com/in/nandini-pajgade-4a3351230
                  </a>
                </>
              }
            />
            <SolutionStep
                title="Aditya Kumawat"
                description={
                  <>Explore My LinkedIn Profile for More Insights <br/>
                    <a href="https://www.linkedin.com/in/adityakumawat2004" target="_blank" rel="noopener noreferrer">
                      www.linkedin.com/in/adityakumawat2004
                    </a>
                  </>
                }
              />
      </div>
    </div>
  );
}

export default About;
