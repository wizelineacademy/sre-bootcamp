package com.wizeline;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import static com.wizeline.JsonUtil.json;
import static spark.Spark.*;

public class App {

    private static final Logger log = LoggerFactory.getLogger(App.class);

    public static void main(String[] args) {

        log.info("Listening on: http://localhost:8000/");

        port(8000);
        get("/", App::routeRoot);
        get("/_health", App::routeRoot);
        post("/login", App::urlLogin, json());
        get("/protected", App::protect, json());
    }

    public static Object routeRoot(spark.Request req, spark.Response res) throws Exception {
        return "OK";
    }

    public static Object urlLogin(spark.Request req, spark.Response res) throws Exception {
        String username = req.queryParams("username");
        String password = req.queryParams("password");
        Response r = new Response(Methods.generateToken(username, password));
        res.type("application/json");
        return r;
    }

    public static Object protect(spark.Request req, spark.Response res) throws Exception {
        String authorization = req.headers("Authorization");
        Response r = new Response(Methods.accessData(authorization));
        res.type("application/json");
        return r;
    }
}
