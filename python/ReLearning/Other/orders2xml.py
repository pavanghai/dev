import csv
# with open('orders.csv') as csvfile:
#     csvoutput = csv.reader(csvfile, delimiter=',')
#     for row in csvoutput:
#         print(type(row))
csvoutputlist = []
with open('orders.csv') as csvfile:
    csvoutput = csv.DictReader(csvfile, delimiter=',')
    for row in csvoutput:
        print(row['OrganizationName'], row['ScheduledEarlyPickup'], row['WeightValue3'])
        csvoutputlist.append(row)
row_list = []
with open('orderxmlfile.txt', 'w') as txtfile:
    for row in row_list:
        txtfile.write(f"""<Order>
    <OrganizationName>{row['OrganizationName']}</OrganizationName>
    <OrdNum>{row['OrdNum']}</OrdNum>
    <OrdType>{row['OrdType']}</OrdType>
    <OrderTMSStatus>{row['OrderTMSStatus']}</OrderTMSStatus>
    <FreightTerms>{row['FreightTerms']}</FreightTerms>
    <IsPrePayment>{row['IsPrePayment']}</IsPrePayment>
    <ScheduledEarlyPickup>{row['ScheduledEarlyPickup']}</ScheduledEarlyPickup>
    <ScheduledEarlyDelivery>{row['ScheduledEarlyDelivery']}</ScheduledEarlyDelivery>
    <TotalGrossWeight>
        <WeightValue uom="{row['uom']}">{row['WeightBase']}</WeightValue>
        <WeightBase uom="Lb">30000</WeightBase>
    </TotalGrossWeight>
    <TotalNetWeight>
        <WeightValue uom="Lb">30000</WeightValue>
        <WeightBase uom="Lb">30000</WeightBase>
    </TotalNetWeight>
    <TotalGrossVolume>
        <VolumeValue uom="CuFt">2100</VolumeValue>
        <VolumeBase uom="CuFt">2100</VolumeBase>
    </TotalGrossVolume>
    <TotalNetVolume>
        <VolumeValue uom="CuFt">2100</VolumeValue>
        <VolumeBase uom="CuFt">2100</VolumeBase>
    </TotalNetVolume>
    <TotalPieceCount>2100</TotalPieceCount>
    <TotalHandlingUnitCount>26</TotalHandlingUnitCount>
    <IsInPlanning>false</IsInPlanning>
    <AreTotalsOverridden>false</AreTotalsOverridden>
    <FreightValue>
        <CurrencyValue uom="USD">0</CurrencyValue>
        <CurrencyBase uom="USD">0</CurrencyBase>
    </FreightValue>
    <IsHot>false</IsHot>
    <IsHazmat>false</IsHazmat>
    <BillingStatus>New</BillingStatus>
    <IntegrationStatus>New</IntegrationStatus>
    <OriginLocNum>DC_OH</OriginLocNum>
    <OriginLoc>
        <OrganizationName>My-Organization</OrganizationName>
        <TradingPartnerNum>Test</TradingPartnerNum>
        <TradingPartnerType>Client</TradingPartnerType>
        <LocNum>DC_OH</LocNum>
        <LocationType>ShipReceive</LocationType>
        <IsActive>true</IsActive>
        <IsBillTo>false</IsBillTo>
        <IsRemitTo>false</IsRemitTo>
        <IsCorporate>false</IsCorporate>
        <AddrName>DC_OH</AddrName>
        <Addr1>--</Addr1>
        <CityName>Hamilton</CityName>
        <StateCode>OH</StateCode>
        <CountryISO2>US</CountryISO2>
        <PostalCode>45014</PostalCode>
        <CalendarName>Mon-Fri-8-5</CalendarName>
        <CalendarAppointmentName>24/7 Appointment</CalendarAppointmentName>
        <AllowsHazmat>false</AllowsHazmat>
        <IsDeliveryAptRequired>false</IsDeliveryAptRequired>
        <IsPickupAptRequired>false</IsPickupAptRequired>
    </OriginLoc>
    <DestinationLocNum>CZ_906</DestinationLocNum>
    <DestinationLoc>
        <OrganizationName>My-Organization</OrganizationName>
        <TradingPartnerNum>Test</TradingPartnerNum>
        <TradingPartnerType>Client</TradingPartnerType>
        <LocNum>CZ_906</LocNum>
        <LocationType>ShipReceive</LocationType>
        <IsActive>true</IsActive>
        <IsBillTo>false</IsBillTo>
        <IsRemitTo>false</IsRemitTo>
        <IsCorporate>false</IsCorporate>
        <AddrName>7-ELEVEN CDC C/O GENESIS LOGISTICS</AddrName>
        <Addr1>--</Addr1>
        <CityName>Santa Fe Springs</CityName>
        <StateCode>CA</StateCode>
        <CountryISO2>US</CountryISO2>
        <PostalCode>90670</PostalCode>
        <CalendarName>Mon-Fri-8-5</CalendarName>
        <CalendarAppointmentName>24/7 Appointment</CalendarAppointmentName>
        <AllowsHazmat>false</AllowsHazmat>
        <IsDeliveryAptRequired>false</IsDeliveryAptRequired>
        <IsPickupAptRequired>false</IsPickupAptRequired>
    </DestinationLoc>
    <Client>
        <OrganizationName>My-Organization</OrganizationName>
        <TradingPartnerNum>Test</TradingPartnerNum>
        <TradingPartnerName>Test</TradingPartnerName>
        <TradingPartnerType>Client</TradingPartnerType>
        <IsActive>true</IsActive>
    </Client>
    <OrderLines>
        <OrderLine>
            <OrdLineNum>1</OrdLineNum>
            <WeightGross>
                <WeightValue uom="Lb">30000</WeightValue>
                <WeightBase uom="Lb">30000</WeightBase>
            </WeightGross>
            <WeightNet>
                <WeightValue uom="Lb">30000</WeightValue>
                <WeightBase uom="Lb">30000</WeightBase>
            </WeightNet>
            <VolumeGross>
                <VolumeValue uom="CuFt">2100</VolumeValue>
                <VolumeBase uom="CuFt">2100</VolumeBase>
            </VolumeGross>
            <VolumeNet>
                <VolumeValue uom="CuFt">2100</VolumeValue>
                <VolumeBase uom="CuFt">2100</VolumeBase>
            </VolumeNet>
            <PieceCount>1170</PieceCount>
            <HandlingUnitCount>26</HandlingUnitCount>
            <IsHazmat>false</IsHazmat>
        </OrderLine>
    </OrderLines>
    </Order>""")    
