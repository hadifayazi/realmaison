import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const propertiesApi = createApi({
  reducerPath: "propertiesApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000/api/v1/properties/",
    // prepareHeaders: (headers) => {
    //   headers.set("Access-Control-Allow-Origin", "true");
    //   headers.set("Content-Type", "application/json");
    //   headers.set("Accept", "application/json");
    //   headers.set("mode", "cors");

    //   return headers;
    // },
  }),
  endpoints: (builder) => ({
    getProperties: builder.query({
      query: () => {
        return {
          url: "",
          method: "GET",
          credentials: "include",
        };
      },
    }),
  }),
});

export const { useGetPropertiesQuery } = propertiesApi;
