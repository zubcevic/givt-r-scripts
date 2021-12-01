package com.zubcevic.givt.rest.client;

import io.quarkus.test.junit.QuarkusTest;
import org.junit.jupiter.api.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.Matchers.greaterThan;
import static org.hamcrest.CoreMatchers.hasItem;


@QuarkusTest
public class GivtResourceTest {

    @Test
    public void testHelloEndpoint() {
        given()
          .when()
            .get("/givt/id/io.quarkus:quarkus-rest-client") // /api/extensions?id=io.quarkus:quarkus-rest-client
          .then()
             .log().all()
             .statusCode(200)
             .body(
                 "$.size()", is(1), // array with 1 json doc
                 "[0].Name", is("PKN Nieuwegein Noord") );
    }

}