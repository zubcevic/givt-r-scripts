package com.zubcevic.givt.rest.client;

import org.eclipse.microprofile.rest.client.annotation.RegisterProvider;
import org.eclipse.microprofile.rest.client.inject.RegisterRestClient;

import io.quarkus.oidc.client.filter.OidcClientFilter;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.QueryParam;

import java.util.List;
import java.util.Set;

@RegisterRestClient(configKey = "service-api")
//@RegisterProvider(OidcClientRequestCustomFilter.class)
@OidcClientFilter
public interface GivtService {

    @GET
    @Path("/CollectGroupView/CollectGroup")
    Set<CollectGroup> getCollectGroup();

    class CollectGroup {
        public String OrgId;
        public String GUID;
        public String Name;
    }
}
