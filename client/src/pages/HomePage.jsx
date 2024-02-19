// import Accordion from "react-bootstrap/Accordion";
import SEO from "../components/shared/SEO";

const HomePage = () => {
  return (
    <>
      <SEO
        title="RealMaison real estate"
        description="Buy, sell or rent a property"
      />
      <div className="background">
        <div className="main-container">
          <section className="first-section">
            <div className="invite">
              <div className="invite-intro">
                <h4>A place called home: buy, rent or sell</h4>{" "}
              </div>
              <div>
                <a href="/properties">
                  <button className="invite-btn">
                    <h5>Start here</h5>
                  </button>
                </a>
              </div>
            </div>
          </section>
          <section className="second-section">
            <div>
              <div className="section2-items">
                <img
                  style={{ width: "300px", height: "200px" }}
                  src="assets/sean-pollock-PhYq704ffdA-unsplash.jpg"
                  alt="apartement"
                />
                <p>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo
                  quae, facilis vitae voluptas corporis perferendis quam culpa
                  enim aliquid, nesciunt tempore officiis blanditiis. Facere
                  odio eveniet doloribus neque numquam unde!
                </p>
              </div>
              <div className="section2-items">
                <img
                  style={{ width: "300px", height: "200px" }}
                  src="assets/webaliser-_TPTXZd9mOo-unsplash.jpg"
                  alt="apartement"
                />
                <p>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo
                  quae, facilis vitae voluptas corporis perferendis quam culpa
                  enim aliquid, nesciunt tempore officiis blanditiis. Facere
                  odio eveniet doloribus neque numquam unde!
                </p>
              </div>
              <div className="section2-items">
                <img
                  style={{ width: "300px", height: "200px" }}
                  src="assets/maria-ziegler-jJnZg7vBfMs-unsplash.jpg"
                  alt="apartement"
                />
                <p>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo
                  quae, facilis vitae voluptas corporis perferendis quam culpa
                  enim aliquid, nesciunt tempore officiis blanditiis. Facere
                  odio eveniet doloribus neque numquam unde!
                </p>
              </div>
            </div>
          </section>
        </div>
      </div>
    </>
  );
};

export default HomePage;
