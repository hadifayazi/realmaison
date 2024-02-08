import { useGetPorpertyDetailsQuery } from "../store/index";
import { useParams } from "react-router-dom";

const PropertyDetails = () => {
  const { slug } = useParams();
  const { data, error, isLoading, isSuccess } =
    useGetPorpertyDetailsQuery(slug);
  console.log(data);

  return <div>details</div>;
};

export default PropertyDetails;
