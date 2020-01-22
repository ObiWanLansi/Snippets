package com.github.obiwanlansi.javalin.helloworld;


import java.util.Date;

import io.javalin.Javalin;



/**
 * The Class MyFirstRestServer Is For ...
 *
 */
final public class MyFirstRestServer {

    /**
     * @param args
     */
    public static void main( final String[] args ) {

        System.out.println(String.format("Server Startet @ %s", new Date()));

        final Javalin app = Javalin.create().start(4242);
        app.get("/", ctx -> ctx.result("Hello World"));
    }

} // end final public class MyFirstRestServer
