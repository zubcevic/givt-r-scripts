package com.zubcevic.givt.rest.client;

import io.quarkus.test.junit.QuarkusTest;
import org.eclipse.microprofile.rest.client.inject.RestClient;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import javax.inject.Inject;
import java.util.Set;

@QuarkusTest
public class MyRemoteServiceTest {

    @Inject
    @RestClient
    GivtService myRemoteService;

   // @Test
    public void testExtensionsRestClientEndpoint() {
        Set<GivtService.CollectGroup> restClientExtensions = myRemoteService.getCollectGroup();

        Assertions.assertEquals(1, restClientExtensions.size());
        for (GivtService.CollectGroup extension : restClientExtensions) {
            Assertions.assertEquals("io.quarkus:quarkus-rest-client", extension.OrgId);
            Assertions.assertEquals("REST Client", extension.Name);
        }
    }
}
