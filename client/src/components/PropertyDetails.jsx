import { useState } from "react";
import { useGetPorpertyDetailsQuery } from "../store/index";
import { useParams } from "react-router-dom";
import { FaArrowAltCircleRight, FaArrowAltCircleLeft } from "react-icons/fa";
import { nanoid } from "@reduxjs/toolkit";
import SEO from "./shared/SEO";

const PropertyDetails = () => {
  const [imageIdx, setImageIdx] = useState(0);
  const { slug } = useParams();
  const { data, error, isLoading } = useGetPorpertyDetailsQuery(slug);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  const sideImage = data.images.map((i, index) => (
    <button
      style={{
        display: "flex",
        flexDirection: "column",
        margin: "2px",
        border: "1px solid transparent",
      }}
      key={nanoid()}
      className="side-image"
      onClick={() => setImageIdx(index)}
    >
      <img
        src={i.image}
        alt={data.title}
        style={{ width: "150px", height: "100px" }}
      />
    </button>
  ));

  return (
    <div>
      <SEO title={data.title} description={data.description} />
      <div style={{ display: "flex" }}>
        <div>
          <>{sideImage}</>
        </div>
        <div style={{ position: "relative" }}>
          <div
            style={{
              backgroundImage: `url(${data.images[imageIdx].image})`,
              backgroundSize: "cover",
              backgroundRepeat: "no-repeat",
              backgroundPosition: "center",
              width: "880px",
              height: "500px",
            }}
          ></div>
          <div style={{ display: "flex", justifyContent: "space-between" }}>
            <button
              style={{
                position: "absolute",
                top: "235px",
                right: "30px",
                backgroundColor: "transparent",
                opacity: "50%",
                border: "none",
                borderRadius: "50%",
              }}
              onClick={() =>
                setImageIdx((prev) => (prev + 1) % data.images.length)
              }
            >
              <FaArrowAltCircleRight style={{ fontSize: "30px" }} />
            </button>
            <button
              style={{
                position: "absolute",
                top: "235px",
                left: "30px",
                backgroundColor: "transparent",
                opacity: "50%",
                border: "none",
                borderRadius: "50%",
              }}
              onClick={() =>
                setImageIdx(
                  (prev) => (prev - 1 + data.images.length) % data.images.length
                )
              }
            >
              <FaArrowAltCircleLeft style={{ fontSize: "30px" }} />
            </button>
          </div>
        </div>
      </div>

      <div>
        <h1>Title: {data.title}</h1>
        <h5>Reference: {data.reference}</h5>
        <p>Country: {data.country}</p>
        <p>State: {data.state}</p>
        <p>Address: {data.address} </p>
        <p>City: {data.city}</p>
        <p>Zipcode: {data.zipcode}</p>
        <p>Type: {data.house_type}</p>
        <p>Surface: {data.surface} m²</p>
        <p>Price: {data.price} €</p>
        <p>Number of bedrooms: {data.bedrooms}</p>
        <p>Number of bathrooms: {data.bathrooms}</p>
        <p>Bumber of views: {data.views}</p>
      </div>
      <div>
        <h5>Description:</h5>
        <p>{data.description}</p>
      </div>
    </div>
  );
};

export default PropertyDetails;
