import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const propertiesApi = createApi({
  reducerPath: "propertiesApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000/api/v1/properties/",
    prepareHeaders: (headers) => {
      headers.append(
        "Authorization",
        "Bearer " +
          "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3MzM2MTY5LCJpYXQiOjE3MDczMjg5NjksImp0aSI6IjJmYTQ3MzcyM2NhZTRlMTA5YTI1ZmE1YTk5NmMzNWIyIiwidXNlcl9pZCI6OH0.fD4qGjontct3snUbWiEV_0Wt2FjTNF1qaI5RQwPrMt8"
      );

      return headers;
    },
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
    getRealtorProperties: builder.query({
      query: () => {
        return {
          url: "realtor",
          method: "GET",
          credentials: "include",
        };
      },
    }),
  }),
});

export const { useGetPropertiesQuery, useGetRealtorPropertiesQuery } =
  propertiesApi;
