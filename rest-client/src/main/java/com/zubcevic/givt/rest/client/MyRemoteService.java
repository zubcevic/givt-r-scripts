package com.zubcevic.givt.rest.client;

import org.eclipse.microprofile.rest.client.inject.RegisterRestClient;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.QueryParam;

import java.util.List;
import java.util.Set;

@RegisterRestClient(configKey = "service-api")
public interface MyRemoteService {

    @GET
    @Path("/extensions")
    Set<Extension> getById(@QueryParam("id") String id);

    class Extension {
        public String id;
        public String name;
        public String shortName;
        public List<String> keywords;
    }
}
